import os

from designs.select_dialog_design import Ui_greeting_dialog

from main_menu import MainWindow
from camera_error_dialog import CameraErrorDialog

import cv2

from PySide6 import QtWidgets, QtGui, QtCore


class StartWindow(QtWidgets.QDialog, Ui_greeting_dialog):
    def __init__(self):
        # установка атрибутов окна
        super().__init__()
        self.camera_error_window = None
        self.main_window = None
        self.setupUi(self)
        self.save_path = os.path.abspath('user_data')

        # установка иконки окна
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        # для ответа на нажатие кнопок
        self.use_file.clicked.connect(self.browse_files)
        self.create_file.clicked.connect(self.make_photo)

    def browse_files(self):
        """Открытие окна выбора файла, переход в главное меню с этим изображением."""
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите .png или .jpeg файл", filter="Изображение ("
                                                                                                        "*.png *.jpg)")

        if directory[0]:
            self.open_main_window(directory[0][0])

    def make_photo(self):
        """Создание фото пользователя и переход в главное меню с этим фото.
        При неудаче - вывод сообщения."""
        # запуск первой камеры
        cap = cv2.VideoCapture(0)

        # если камера не сработала
        if not cap.isOpened():
            self.open_camera_error_window()
        else:
            #  подготовка камеры
            for i in range(30):
                cap.read()

            # фиксирование фото
            ret, frame = cap.read()

            # запись в файл
            is_success, frame_arr = cv2.imencode(".png", frame)
            frame_arr.tofile(self.save_path + r'\camera.png', format='png')

            cap.release()

            # запускаем следующее окно
            self.open_main_window(self.save_path + r'\camera.png')

    def open_main_window(self, file: str):
        """Открытие главного окна."""
        self.main_window = MainWindow(file)
        self.main_window.show()
        self.hide()

    def open_camera_error_window(self):
        """Открытие окна с сообщением об ошибке использования камеры"""
        self.camera_error_window = CameraErrorDialog()
        self.camera_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.camera_error_window.show()
