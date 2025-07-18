from enum import Enum
import threading
from typing import Any, Callable, List, Optional
import typing

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
import asyncio

from PyQt6.QtCore import pyqtSignal
from core.base_object import BaseObject
from utils.common_utils import CommonUtils
from pydantic import BaseModel


class WebSocketManager(BaseObject):

    class WebSocketConnection(Enum):
        CLIENT_LOG: str = "client_log"
        PROCESS_PROGRESS: str = "process_progress"

    def __init__(self, log_to_ui_func: Optional[Callable] = None):
        super().__init__(log_to_ui_func=log_to_ui_func)
        self.active_connections: dict[self.WebSocketConnection.value, WebSocket] = {}

    async def connect(self, con: WebSocketConnection, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[con.value] = websocket
        self.log_info("WebSocket客户端已连接")

    def disconnect(self, con: WebSocketConnection):
        if con.value in self.active_connections:
            self.active_connections[con.value] = None
            self.log_info("WebSocket客户端断开连接")

    async def close_all_connections(self):
        for _, websocket in self.active_connections.copy().items():
            if websocket is not None:
                try:
                    if hasattr(websocket, "client_state") and websocket.client_state.name != "CLOSED":
                        await websocket.close()
                except Exception as e:
                    self.log_warning(f"websocket关闭连接失败：{e}")
            self.active_connections.clear()

    async def send_message(self, con: WebSocketConnection, message: str):
        try:
            if self.active_connections.get(con.value) is not None:
                await self.active_connections[con.value].send_text(message)
        except WebSocketDisconnect:
            self.disconnect(con=con)

    async def handle_client_log(self, websocket: WebSocket):
        await self.connect(self.WebSocketConnection.CLIENT_LOG, websocket=websocket)
        try:
            while True:
                try:
                    data = await websocket.receive_text()
                    self.log_info(f"receive_text: {data}")
                except WebSocketDisconnect:
                    break
        finally:
            self.disconnect(self.WebSocketConnection.CLIENT_LOG)

    async def handle_process_progress(self, websocket: WebSocket):
        await self.connect(self.WebSocketConnection.PROCESS_PROGRESS, websocket=websocket)
        try:
            while True:
                try:
                    data = await websocket.receive_text()
                    self.log_info(f"receive_text: {data}")
                except WebSocketDisconnect:
                    break
        finally:
            self.disconnect(self.WebSocketConnection.PROCESS_PROGRESS)

    def send(self, con: WebSocketConnection, message: any):
        asyncio.run(self.send_message(con=con, message=CommonUtils.convert_to_str(message=message)))


class ApiServer(BaseObject):

    scan_signal = pyqtSignal()
    add_signal = pyqtSignal(list)
    start_signal = pyqtSignal()
    stop_signal = pyqtSignal()
    clear_signal = pyqtSignal()
    selectLang_signal = pyqtSignal(str, str)
    exit_signal = pyqtSignal()

    def __init__(self, log_to_ui_func: Optional[Callable] = None) -> None:
        super().__init__(log_to_ui_func=log_to_ui_func)
        self.app = FastAPI(title="AILiteSubtitler API Server")
        self.server = None
        self.server_thread = None
        self.ws = None
        self._route()
        self._route_ws()

    def run(self, host: str = "0.0.0.0", port: int = 10000):
        self._create_server_(host, port)
        try:
            self.server_thread.start()
            self.log_info(f"API服务启动监听：http://{host}:{port}")
        except Exception as e:
            self.log_warning(f"API服务监听失败：{e}")

    def active(self) -> bool:
        return self.ws is not None and self.server is not None and self.server_thread is not None

    def shutdown(self):
        if self.server is not None:
            self.server.should_exit = True
        del self.ws
        del self.server
        del self.server_thread
        self.ws = None
        self.server = None
        self.server_thread = None
        self.log_info(f"API服务停止监听")

    def request_scan_connect(self, callback_func):
        self.scan_signal.connect(callback_func)

    def request_add_connect(self, callback_func):
        self.add_signal.connect(callback_func)

    def request_start_connect(self, callback_func):
        self.start_signal.connect(callback_func)

    def request_stop_connect(self, callback_func):
        self.stop_signal.connect(callback_func)

    def request_clear_connect(self, callback_func):
        self.clear_signal.connect(callback_func)

    def request_selectLang_connect(self, callback_func):
        self.selectLang_signal.connect(callback_func)

    def request_exit_connect(self, callback_func):
        self.exit_signal.connect(callback_func)

    def response_call(self, con: WebSocketManager.WebSocketConnection, arg: any):
        if self.active() is False:
            return
        self.ws.send(con=con, message=arg)

    def route(self, path: str, endpoint: Callable[..., Any], methods: List[str] | None) -> None:
        self.app.add_api_route(path=path, endpoint=endpoint, methods=methods)

    def route_ws(self, path: str, route: typing.Callable[[WebSocket], typing.Awaitable[None]]) -> None:
        self.app.add_websocket_route(path=path, route=route)

    def _create_server_(self, host: str = "0.0.0.0", port: int = 10000):
        if self.active() is True:
            return
        self.server = uvicorn.Server(uvicorn.Config(app=self.app, host=host, port=port, reload=False))
        self.server_thread = threading.Thread(target=self.server.run)
        self.server_thread.daemon = True
        self.ws = WebSocketManager(log_to_ui_func=self.log_to_ui_func)

    def _route(self) -> None:
        self.route(path="/scan", endpoint=self._request_scan, methods=["GET"])
        self.route(path="/add", endpoint=self._request_add, methods=["POST"])
        self.route(path="/start", endpoint=self._request_start, methods=["GET"])
        self.route(path="/stop", endpoint=self._request_stop, methods=["GET"])
        self.route(path="/clear", endpoint=self._request_clear, methods=["GET"])
        self.route(path="/lang", endpoint=self._request_selectLang, methods=["GET"])
        self.route(path="/exit", endpoint=self._request_exit, methods=["GET"])

    def _route_ws(self) -> None:
        self.route_ws("/log", self._request_log)
        self.route_ws("/process", self._request_process_progress)

    def _request_scan(self):
        self.scan_signal.emit()
        return {"code": 1, "message": "success", "type": "scan"}

    class AddFilenamesItem(BaseModel):
        count: int
        filenames: list[str]

    def _request_add(self, data: AddFilenamesItem):
        if data.count > 0 and len(data.filenames) > 0:
            self.add_signal.emit(data.filenames)
            return {"code": 1, "message": "success", "type": "add"}
        else:
            return {"code": 0, "message": "failed", "type": "add"}

    def _request_start(self):
        self.start_signal.emit()
        return {"code": 1, "message": "success", "type": "start"}

    def _request_stop(self):
        self.stop_signal.emit()
        return {"code": 1, "message": "success", "type": "stop"}

    def _request_clear(self):
        self.clear_signal.emit()
        return {"code": 1, "message": "success", "type": "clear"}

    def _request_selectLang(self, source: str = "", target: str = ""):
        self.selectLang_signal.emit(source, target)
        return {"code": 1, "message": "success", "type": "lang"}

    def _request_exit(self):
        self.exit_signal.emit()
        return {"code": 1, "message": "success", "type": "exit"}

    async def _request_log(self, websocket: WebSocket):
        await self.ws.handle_client_log(websocket)

    async def _request_process_progress(self, websocket: WebSocket):
        await self.ws.handle_process_progress(websocket)
