import cv2
import numpy

from designs.degree_dialog_design import Ui_degree_dialog

from PySide6 import QtGui
from PySide6.QtWidgets import QDialog


class DegreeDialog(QDialog, Ui_degree_dialog):
    def __init__(self, main_window):
        # установка атрибутов окна
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        # установка иконки окна
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        # для отображения текущего значения угла
        self.degree_slider.sliderMoved.connect(self.update_degree_counter)
        self.degree_slider.sliderReleased.connect(self.update_degree_counter)

        # для работы с кнопками
        self.buttons.accepted.connect(self.provide_angle)
        self.buttons.rejected.connect(self.cancel_operation)

    def update_degree_counter(self):
        """Обновление показателя угла наклона."""
        self.degree_counter.setText(str(self.degree_slider.value()))

    def provide_angle(self):
        """Создает изображение с заданным углом поворота и показывает его."""
        degree = int(self.degree_slider.value())

        pic_to_edit = open(self.main_window.current_picture, "rb")
        picture_arr = numpy.frombuffer(pic_to_edit.read(), dtype=numpy.uint8)
        picture = cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)

        # получение повернутого изображения
        (height, weight) = picture.shape[:2]
        center = (int(weight / 2), int(height / 2))

        if degree in [360, 180]:
            rotation_matrix = cv2.getRotationMatrix2D(center, degree, 1)
        else:
            rotation_matrix = cv2.getRotationMatrix2D(center, degree, 0.6)
        rotated_picture = cv2.warpAffine(picture, rotation_matrix, (weight, height))

        # сохранение изображения
        is_success, rotated_pic_arr = cv2.imencode(".png", rotated_picture)
        rotated_pic_arr.tofile(self.main_window.save_path + r'\rotated.png', format='png')

        self.main_window.picture.setPixmap(
            QtGui.QPixmap(self.main_window.save_path + r'\rotated.png').scaled(self.main_window.picture.width(),
                                                                               self.main_window.picture.height())
        )
        self.main_window.current_picture = self.main_window.save_path + r'\rotated.png'
        self.hide()

    def cancel_operation(self):
        self.hide()
