from PyQt4 import QtCore, QtGui, uic

class SignInPage(QtGui.QMainWindow):
    def __init__(self):
        super(SignInPage, self).__init__()

        uic.loadUi("ui/signin.ui", self)

        self.show()