# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, picture: str):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 677))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionBox = QtWidgets.QComboBox(self.centralwidget)
        self.optionBox.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.optionBox.setEditable(False)
        self.optionBox.setObjectName("optionBox")
        self.optionBox.addItem("")
        self.optionBox.addItem("")
        self.optionBox.addItem("")
        self.optionBox.addItem("")
        self.verticalLayout.addWidget(self.optionBox)
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(picture))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.verticalLayout.addWidget(self.picture)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_sharpness = QtGui.QAction(MainWindow)
        self.add_sharpness.setObjectName("add_sharpness")
        self.change_angle = QtGui.QAction(MainWindow)
        self.change_angle.setObjectName("change_angle")
        self.paint_line = QtGui.QAction(MainWindow)
        self.paint_line.setObjectName("paint_line")
        self.change_picture = QtGui.QAction(MainWindow)
        self.change_picture.setObjectName("change_picture")
        self.menu.addAction(self.add_sharpness)
        self.menu.addAction(self.change_angle)
        self.menu.addAction(self.paint_line)
        self.menu.addAction(self.change_picture)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyEdit"))
        self.optionBox.setItemText(0, _translate("MainWindow", "Оригинальное изображение"))
        self.optionBox.setItemText(1, _translate("MainWindow", "Красный канал изображения"))
        self.optionBox.setItemText(2, _translate("MainWindow", "Зеленый канал изображения"))
        self.optionBox.setItemText(3, _translate("MainWindow", "Синий канал изображения"))
        self.menu.setTitle(_translate("MainWindow", "Редактировать"))
        self.add_sharpness.setText(_translate("MainWindow", "Повысить резкость"))
        self.change_angle.setText(_translate("MainWindow", "Повернуть изображение на введенный угол"))
        self.paint_line.setText(_translate("MainWindow", "Нарисовать линию"))
        self.change_picture.setText(_translate("MainWindow", "Сменить изображение"))
