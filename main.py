import sys

from PyQt5 import QtWidgets


# from widgets.mainwindow import MainWindow
from widgets.frmmain import FrmMain


def enter_point():
    app = QtWidgets.QApplication(sys.argv)
    # widget = QtWidgets.QWidget()
    # widget.resize(400, 100)
    # widget.setWindowTitle("This is a demo for PyQt Widget.")
    # widget.show()
    # window = MainWindow(None, None)
    # window.show()
    window = FrmMain(None, None)
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    enter_point()
