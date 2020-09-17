from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QWidget, QDialog, QPlainTextEdit, QSpinBox, QHBoxLayout, QVBoxLayout, QComboBox, \
    QCompleter, QLabel, QStatusBar, QStyleOption
from PySide2.QtGui import QPainter,QColor,QFont
from qtpy import QtGui


class BottomWidget(QWidget):
    def __init__(self, parent, title_visible=True, author_visible=True):
        super(BottomWidget, self).__init__(parent)
        self._title_visible = title_visible
        self._author_visible = author_visible
        self.title = "burn_tool"
        self.version = "V1.0"
        self.author = "zhaoqi"
        self.fontName = "Microsoft Yahei"
        self.fontSize = 9

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        # o = QStyleOption()
        # o.initFrom(self)
        # p = QPainter()
        pass

    @property
    def title_visible(self):
        return self._title_visible

    @title_visible.setter
    def title_visible(self, title_visible):
        self._title_visible = title_visible

    @property
    def author_visible(self):
        return self._author_visible

    @author_visible.setter
    def author_visible(self, author_visible):
        self._author_visible = author_visible

    def start(self):
        lab_title = QLabel(self)
        lab_title.setText("欢迎使用{} {}".format(self.title, self.version))

        layout = QHBoxLayout(self)
        layout.setSpacing(6)
        layout.setContentsMargins(6, 6, 6, 6)

        if self._title_visible is True:
            layout.addWidget(lab_title)

