import sys

from PySide6.QtWidgets import QApplication

from select_dialog import StartWindow


def main():
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
