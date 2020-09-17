from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter, QAction
from PyQt5.QtGui import QKeySequence, QDesktopServices
from PyQt5.QtCore import QTimer, Qt, QUrl

from widgets.qui.bottomwidget import BottomWidget
from widgets.ui.frmmain import Ui_frmMain


class FrmMain(QWidget, Ui_frmMain):
    MAX_SUCCESSIVE_NODE_ERRORS = 1000

    # noinspection PyTypeChecker,PyCallByClass,PyUnresolvedReferences
    def __init__(self, node, iface_name):
        # Parent
        super(FrmMain, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('UAVCAN GUI Tool')
        self.resize(800, 480)
        self.bottomWidget.start()
