import sys

from PySide2 import QtWidgets


# from widgets.mainwindow import MainWindow
from widgets.frmmain import FrmMain


def enter_point():
    app = QtWidgets.QApplication(sys.argv)
    window = FrmMain(None, None)
    window.show()
    app.exec_()


if __name__ == "__main__":
    enter_point()
