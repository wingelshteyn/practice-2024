"""Модуль, который содержит в себе сборку начального окна выбора"""

from PySide6 import QtCore, QtWidgets, QtGui


class Ui_greeting_dialog(object):
    def setupUi(self, greeting_dialog):
        greeting_dialog.setObjectName("greeting_dialog")
        greeting_dialog.resize(440, 252)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(greeting_dialog.sizePolicy().hasHeightForWidth())
        greeting_dialog.setSizePolicy(sizePolicy)
        greeting_dialog.setMinimumSize(QtCore.QSize(400, 200))
        greeting_dialog.setMaximumSize(QtCore.QSize(440, 252))
        greeting_dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        greeting_dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        greeting_dialog.setSizeGripEnabled(False)
        greeting_dialog.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(greeting_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info = QtWidgets.QTextBrowser(greeting_dialog)
        self.info.setEnabled(True)
        self.info.setMinimumSize(QtCore.QSize(420, 200))
        self.info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_file = QtWidgets.QPushButton(greeting_dialog)
        self.create_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.create_file.setCheckable(True)
        self.create_file.setObjectName("create_file")
        self.horizontalLayout.addWidget(self.create_file)
        self.use_file = QtWidgets.QPushButton(greeting_dialog)
        self.use_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.use_file.setCheckable(True)
        self.use_file.setObjectName("use_file")
        self.horizontalLayout.addWidget(self.use_file)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(greeting_dialog)
        QtCore.QMetaObject.connectSlotsByName(greeting_dialog)

    def retranslateUi(self, greeting_dialog):
        _translate = QtCore.QCoreApplication.translate
        greeting_dialog.setWindowTitle(_translate("greeting_dialog", "Добро пожаловать!", "Welcome!"))
        self.info.setHtml(_translate("greeting_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Выберите опцию, которая вам подходит для </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">работы с приложением</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">ВНИМАНИЕ: сделать снимок не получится без подключенной видеокамеры, а</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">для работы требуются файлы формата </span><span style=\" font-size:10pt; font-weight:700;\">png</span><span style=\" font-size:10pt;\"> или </span><span style=\" font-size:10pt; font-weight:700;\">jpeg</span><span style=\" font-size:10pt;\">!</span></p></body></html>"))
        self.create_file.setText(_translate("greeting_dialog", "Сделать снимок"))
        self.use_file.setText(_translate("greeting_dialog", "Использовать файл"))

