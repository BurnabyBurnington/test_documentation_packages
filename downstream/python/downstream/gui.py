"""The main window + widgets for :mod:`downstream`."""

import re

from Qt import QtWidgets
from qt_rez_core import api

from . import module

_HELP_EXPRESSION = re.compile("Documentation")


class Widget(QtWidgets.QWidget):
    """The main GUI contents of :class:`Window`."""

    def __init__(self, parent=None):
        """Track a parent reference, if included.

        Args:
            parent (Qt.QtCore.QObject, optional):
                An object which, if provided, holds a reference to this instance.

        """
        super(Widget, self).__init__(parent=parent)

        self.setLayout(QtWidgets.QVBoxLayout())

        self._title = QtWidgets.QLabel("Some text")
        self._button = QtWidgets.QPushButton("Press me to call dependency functions")

        self.layout().addWidget(self._title)
        self.layout().addWidget(self._button)

        self._button.clicked.connect(module.use_both)


class Window(QtWidgets.QMainWindow):
    """The window which displays whenever a user calls :ref:`python -m downstream`."""

    def __init__(self, parent=None):
        """Track a parent reference, if included.

        Args:
            parent (Qt.QtCore.QObject, optional):
                An object which, if provided, holds a reference to this instance.

        """
        super(Window, self).__init__(parent=parent)

        widget = Widget()
        self.setCentralWidget(widget)

        menu = api.get_current_help_menu(title="Help")
        menu_bar = QtWidgets.QMenuBar()
        menu_bar.addMenu(menu)

        self.setMenuBar(menu_bar)
