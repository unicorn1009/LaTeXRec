import sys

from PyQt5.QtWidgets import *

from myWindow import QmyWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QmyWidget()
    w.show()
    sys.exit(app.exec_())