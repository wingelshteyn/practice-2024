from PySide6 import QtGui

from designs.camera_error_dialog_design import Ui_camera_error_dialog

from PySide6.QtWidgets import QDialog


class CameraErrorDialog(Ui_camera_error_dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # установка иконки окна
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        # для работы с кнопками
        self.ok_button.accepted.connect(self.hide)



