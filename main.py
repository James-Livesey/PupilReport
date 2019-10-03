import sys
from PyQt4 import QtGui

import ui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = ui.SignInPage()

    sys.exit(app.exec_())