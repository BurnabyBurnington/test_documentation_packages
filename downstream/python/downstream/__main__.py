"""Load the main GUI."""

from Qt import QtWidgets

from . import gui

application = QtWidgets.QApplication([])

window = gui.Window()
window.setWindowTitle("Example GUI")
window.show()

application.exec_()
