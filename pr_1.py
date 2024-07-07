import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QSlider, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.processed_image = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Processing App')
        self.layout = QVBoxLayout()
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)
        self.upload_button = QPushButton('Upload Image', self)
        self.upload_button.clicked.connect(self.uploadImage)
        self.layout.addWidget(self.upload_button)

        self.camera_button = QPushButton('Take Photo from Camera', self)
        self.camera_button.clicked.connect(self.takePhoto)
        self.layout.addWidget(self.camera_button)

        self.sharpen_slider = QSlider(Qt.Horizontal)
        self.sharpen_slider.setMinimum(0)
        self.sharpen_slider.setMaximum(100)
        self.sharpen_slider.valueChanged.connect(self.sharpenImage)
        self.layout.addWidget(self.sharpen_slider)
        self.rotation_lineedit = QLineEdit(self)

        self.rotation_lineedit.setPlaceholderText('Enter rotation angle')
        self.layout.addWidget(self.rotation_lineedit)
        self.start_x_lineedit = QLineEdit(self)

        self.start_x_lineedit.setPlaceholderText('Start X coordinate')
        self.layout.addWidget(self.start_x_lineedit)
        self.start_y_lineedit = QLineEdit(self)

        self.start_y_lineedit.setPlaceholderText('Start Y coordinate')
        self.layout.addWidget(self.start_y_lineedit)
        self.end_x_lineedit = QLineEdit(self)

        self.end_x_lineedit.setPlaceholderText('End X coordinate')
        self.layout.addWidget(self.end_x_lineedit)
        self.end_y_lineedit = QLineEdit(self)

        self.end_y_lineedit.setPlaceholderText('End Y coordinate')
        self.layout.addWidget(self.end_y_lineedit)

        self.thickness_lineedit = QLineEdit(self)
        self.thickness_lineedit.setPlaceholderText('Line thickness')
        self.layout.addWidget(self.thickness_lineedit)

        self.rotate_button = QPushButton('Rotate Image', self)
        self.rotate_button.clicked.connect(self.rotateImage)
        self.layout.addWidget(self.rotate_button)

        self.draw_line_button = QPushButton('Draw Line', self)
        self.draw_line_button.clicked.connect(self.drawLine)
        self.layout.addWidget(self.draw_line_button)
        self.setLayout(self.layout)

    def uploadImage(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg)')
        self.image = cv2.imread(file_path)
        self.displayImage(self.image)

    def takePhoto(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        self.image = frame
        cap.release()
        self.displayImage(self.image)



    def displayImage(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.image_label.setPixmap(pixmap)

    def sharpenImage(self):
        if self.image is not None:
            sharpen_val = self.sharpen_slider.value() / 100.0
            kernel = np.array([[-1, -1, -1], [-1, 9 + sharpen_val, -1], [-1, -1, -1]])
            self.processed_image = cv2.filter2D(self.image, -1, kernel)
            self.displayImage(self.processed_image)

    def rotateImage(self):
        if self.processed_image is not None:
            angle = int(self.rotation_lineedit.text())
            rows, cols, _ = self.processed_image.shape
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            self.processed_image = cv2.warpAffine(self.processed_image, M, (cols, rows))
            self.displayImage(self.processed_image)

    def drawLine(self):
        if self.processed_image is not None:
            self.start_x = int(self.start_x_lineedit.text())
            self.start_y = int(self.start_y_lineedit.text())
            self.end_x = int(self.end_x_lineedit.text())
            self.end_y = int(self.end_y_lineedit.text())
            thickness = int(self.thickness_lineedit.text())
            color = (0, 255, 0)
            cv2.line(self.processed_image, (self.start_x, self.start_y),
                     (self.end_x, self.end_y), color, thickness)
            self.displayImage(self.processed_image)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageProcessingApp()
    window.show()
    sys.exit(app.exec_())