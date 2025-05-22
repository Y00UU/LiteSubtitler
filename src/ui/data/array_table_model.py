# coding: utf8
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


class ArrayTableModel(QAbstractTableModel):
    """基于二维数组的表格模型类，继承自 `QAbstractTableModel`。

    该类用于将二维数组数据映射为表格模型，支持动态更新、删除和插入行。

    Attributes:
        data (list): 存储表格数据的二维列表。
        _headers (list): 存储表格列标题的列表。
    """

    def __init__(self, data: list, headers: list, parent=None):
        """初始化实例。

        Args:
            data (list): 二维列表，表示表格数据。
            headers (list): 列表，表示表格的列标题。
            parent (QObject, optional): 父对象，默认为 None。
        """
        super().__init__(parent)
        self.data = data
        self._headers = headers
        self._editable_columns = set()  # 存储可编辑列的索引

    def set_editable_columns(self, columns):
        """设置可编辑列，columns为列索引列表"""
        self._editable_columns = set(columns)
        self.layoutChanged.emit()  # 通知视图更新

    def rowCount(self, parent=QModelIndex()) -> int:
        """返回表格的行数。

        Args:
            parent (QModelIndex): 父索引，默认为空索引。

        Returns:
            int: 表格的行数。
        """
        return len(self.data)

    def columnCount(self, parent=QModelIndex()) -> int:
        """返回表格的列数。

        Args:
            parent (QModelIndex): 父索引，默认为空索引。

        Returns:
            int: 表格的列数。
        """
        return len(self.data[0]) if self.data else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """返回指定索引处的数据。

        Args:
            index (QModelIndex): 数据索引。
            role (Qt.ItemDataRole): 数据角色，默认为 DisplayRole。

        Returns:
            any: 索引处的数据。如果索引无效或角色不匹配，返回 None。
        """
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self.data[index.row()][index.column()]

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            self.data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """返回表头数据。

        Args:
            section (int): 表头部分（行号或列号）。
            orientation (Qt.Orientation): 表头方向（水平或垂直）。
            role (Qt.ItemDataRole): 数据角色，默认为 DisplayRole。

        Returns:
            any: 表头数据。如果角色不匹配，返回 None。
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:  # 列标题
                return self._headers[section]
            elif orientation == Qt.Orientation.Vertical:  # 行标题
                return f"{section + 1}"
        return None

    def flags(self, index):
        """返回指定索引的标志。

        Args:
            index (QModelIndex): 数据索引。

        Returns:
            Qt.ItemFlags: 索引的标志。
        """
        default_flags = super().flags(index)
        if index.column() in self._editable_columns:
            return default_flags | Qt.ItemFlag.ItemIsEditable
        return default_flags
        # if index.isValid():
        #     return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        # return Qt.ItemFlag.NoItemFlags

    def update_data(self, new_data: list):
        """更新表格数据。

        Args:
            new_data (list): 新的二维列表数据。
        """
        self.beginResetModel()
        self.data = new_data
        self.endResetModel()

    def clear(self):
        """清空表格数据。"""
        first = 0
        last = self.rowCount() - 1
        if last >= first:
            self.beginRemoveRows(QModelIndex(), first, last)
            self.data.clear()
            self.endRemoveRows()

    def remove_row(self, row_index: int):
        """删除指定行。

        Args:
            row_index (int): 要删除的行索引。

        Raises:
            QMessageBox: 如果行索引无效，弹出警告对话框。
        """
        if 0 <= row_index < self.rowCount():
            self.beginRemoveRows(QModelIndex(), row_index, row_index)
            self.data.pop(row_index)
            self.endRemoveRows()
        else:
            raise RuntimeError(f"Row index {row_index} is out of range.")

    def append_row(self, row_data: list):
        """在表格末尾添加一行。

        Args:
            row_data (list): 要添加的行数据。
        """
        row_position = self.rowCount()
        # 如果表格中只有一行且第一行的第二列为 '*'，则删除该行
        if row_position == 1 and self.data[0][1] == '*':
            self.remove_row(0)

        self.beginInsertRows(QModelIndex(), row_position, row_position)
        self.data.append(row_data)
        self.endInsertRows()

    def update_cell(self, row_id: str, col_idx: int, col_data):
        """更新指定单元格的数据。

        Args:
            row_id (str): 行的唯一标识。
            col_idx (int): 列索引。
            col_data (any): 新的单元格数据。
        """
        self.beginResetModel()
        for row in self.data:
            if row[0] == row_id:
                row[col_idx] = col_data
                break
        self.endResetModel()

    def update_row(self, row_id: int, row_data: list):
        """更新指定行的数据。

        Args:
            row_id (int): 行的唯一标识。
            row_data (list): 新的行数据。
        """
        self.beginResetModel()
        for row in self.data:
            if row[0] == row_id:
                mi = min(len(row), len(row_data))
                for i in range(1, mi):  # 从第二列开始更新
                    row[i] = row_data[i]
                break
        self.endResetModel()
