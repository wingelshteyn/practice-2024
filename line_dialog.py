import cv2
import numpy

from designs.line_dialog_design import Ui_line_dialog

from PySide6.QtWidgets import QDialog
from PySide6 import QtGui


class LineDialog(Ui_line_dialog, QDialog):
    def __init__(self, main_window):
        # установка атрибутов окна
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        # установка иконки окна
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        # для валидации данных во время ввода пользователем
        self.thickness.textChanged.connect(self.validate_thickness)

        # для работы с кнопками
        self.buttons.accepted.connect(self.draw_line)
        self.buttons.rejected.connect(self.cancel_operation)

    def validate_start_x(self):
        cord = self.start_point_x.toPlainText()
        if cord[0] == '-':
            cord = cord.replace('-', '1', 1)
        if not (cord.isnumeric()):
            self.thickness.setPlainText("0")

    def validate_start_y(self):
        cord = self.start_point_y.toPlainText()
        if cord[0] == '-':
            cord = cord.replace('-', '1', 1)
        if not (cord.isnumeric()):
            self.thickness.setPlainText("0")

    def validate_end_x(self):
        cord = self.end_point_x.toPlainText()
        if cord[0] == '-':
            cord = cord.replace('-', '1', 1)
        if not (cord.isnumeric()):
            self.thickness.setPlainText("0")

    def validate_end_y(self):
        cord = self.end_point_y.toPlainText()
        if cord[0] == '-':
            cord = cord.replace('-', '1', 1)
        if not (cord.isnumeric()):
            self.thickness.setPlainText("0")

    def validate_thickness(self):
        if not (self.thickness.toPlainText().isnumeric()):
            self.thickness.setPlainText("1")

    def draw_line(self):
        """Создает изображение с нарисованной линией и показывает его."""
        pic_to_edit = open(self.main_window.current_picture, "rb")
        picture_arr = numpy.frombuffer(pic_to_edit.read(), dtype=numpy.uint8)
        picture = cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)

        # рисование линии по координатам
        first_x = int(self.start_point_x.toPlainText())
        first_y = int(self.start_point_x.toPlainText())
        last_x = int(self.end_point_x.toPlainText())
        last_y = int(self.end_point_y.toPlainText())

        lined_pic = cv2.line(picture,
                             (first_x, first_y),
                             (last_x, last_y),
                             (0, 225, 0),
                             int(self.thickness.toPlainText()))

        # сохранение изображения
        is_success, lined_pic_arr = cv2.imencode(".png", lined_pic)
        lined_pic_arr.tofile(self.main_window.save_path + r'\lined.png', format='png')

        self.main_window.picture.setPixmap(
            QtGui.QPixmap(self.main_window.save_path + r'\lined.png').scaled(self.main_window.picture.width(),
                                                                             self.main_window.picture.height())
        )
        self.main_window.current_picture = self.main_window.save_path + r'\lined.png'
        self.hide()

    def cancel_operation(self):
        self.hide()
