from PyQt6 import QtWidgets
from core.main_window import MainWindow
import sys


def main():
    """This is where the main window gets initialized.
    """
    app = QtWidgets.QApplication([])

    application = MainWindow()

    application.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()