# coding: utf8
from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QDialog, QLabel

from config import ICON_REC, APP_NAME, APP_TITLE, VERSION, APP_DESC, APP_LICENSE, AUTHOR
from core.base_object import BaseObject
from ui.driver.gui_tool import GuiTool
from ui.gui.about import Ui_dlgAbout


class AboutFacade(BaseObject):
    """About的外观类。"""

    def __init__(self, func_write_log):
        """初始化实例。"""
        super().__init__(log_to_ui_func=func_write_log)

        self.dialog = QDialog()
        self.ui = Ui_dlgAbout()
        self.ui.setupUi(self.dialog)

        self.ui.edtAppName.setText(f"{APP_TITLE}，{APP_NAME}")
        self.ui.edtVersion.setText(f"Version：{VERSION}")
        self.ui.edtAppDesc.setText(f"{APP_DESC}")
        self.ui.edtLicense.setText(f"开源协议：{APP_LICENSE}")
        self.ui.edtAuthor.setText(f"作者：{AUTHOR}")
        self.ui.lblLogo.setPixmap(QtGui.QPixmap(ICON_REC.get("logo")))
        self.ui.btnClose.clicked.connect(lambda: self.dialog.close())

    def show(self) -> None:
        """显示。"""
        # self.dialog.setFixedHeight(580)
        self.dialog.exec()
