# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import images_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1020, 780)
        Dialog.setMinimumSize(QSize(1020, 780))
        Dialog.setMaximumSize(QSize(1020, 780))
        Dialog.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(550, 0))
        self.widget.setMaximumSize(QSize(550, 16777215))
        self.widget.setStyleSheet(u"#widget {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"	border-right: 2px solid rgba(255, 255, 255, 150);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 650))
        self.label.setMaximumSize(QSize(16777215, 650))
        self.label.setStyleSheet(u"QLabel {\n"
"	background-image: url(:/img/30anosNeo.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"")
        self.label.setPixmap(QPixmap(u":/img/implante.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(470, 0))
        self.widget_2.setMaximumSize(QSize(470, 16777215))
        self.widget_2.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 10)
        self.logoNeo = QLabel(self.widget_2)
        self.logoNeo.setObjectName(u"logoNeo")
        self.logoNeo.setMinimumSize(QSize(0, 80))
        self.logoNeo.setMaximumSize(QSize(16777215, 80))
        self.logoNeo.setStyleSheet(u"#logoNeo {\n"
"	margin: 20px 120px 20px;\n"
"}")
        self.logoNeo.setPixmap(QPixmap(u":/img/neodent-logo.png"))
        self.logoNeo.setScaledContents(True)

        self.verticalLayout.addWidget(self.logoNeo)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(465, 250))
        self.frame.setMaximumSize(QSize(465, 250))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.lblColaborador = QLabel(self.frame)
        self.lblColaborador.setObjectName(u"lblColaborador")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblColaborador.sizePolicy().hasHeightForWidth())
        self.lblColaborador.setSizePolicy(sizePolicy)
        self.lblColaborador.setMinimumSize(QSize(0, 20))
        self.lblColaborador.setMaximumSize(QSize(16777215, 20))
        self.lblColaborador.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.lblColaborador, 0, 0, 1, 1)

        self.txtColaborador = QLineEdit(self.frame)
        self.txtColaborador.setObjectName(u"txtColaborador")
        self.txtColaborador.setMinimumSize(QSize(0, 40))
        self.txtColaborador.setMaximumSize(QSize(16777215, 40))
        self.txtColaborador.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fff, stop:1 #f2f2f2);\n"
"	font: 12pt \"Calibri\";\n"
"	color: black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"}")

        self.gridLayout.addWidget(self.txtColaborador, 1, 0, 1, 1)

        self.lblMatricula = QLabel(self.frame)
        self.lblMatricula.setObjectName(u"lblMatricula")
        self.lblMatricula.setMinimumSize(QSize(0, 20))
        self.lblMatricula.setMaximumSize(QSize(16777215, 20))
        self.lblMatricula.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.lblMatricula, 2, 0, 1, 1)

        self.txtMatricula = QLineEdit(self.frame)
        self.txtMatricula.setObjectName(u"txtMatricula")
        self.txtMatricula.setMinimumSize(QSize(0, 40))
        self.txtMatricula.setMaximumSize(QSize(16777215, 40))
        self.txtMatricula.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fff, stop:1 #f2f2f2);\n"
"	font: 12pt \"Calibri\";\n"
"	color: black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"}")

        self.gridLayout.addWidget(self.txtMatricula, 3, 0, 1, 1)

        self.lblSetor = QLabel(self.frame)
        self.lblSetor.setObjectName(u"lblSetor")
        self.lblSetor.setMinimumSize(QSize(0, 20))
        self.lblSetor.setMaximumSize(QSize(16777215, 20))
        self.lblSetor.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.lblSetor, 4, 0, 1, 1)

        self.cmbSetores = QComboBox(self.frame)
        self.cmbSetores.setObjectName(u"cmbSetores")
        self.cmbSetores.setMinimumSize(QSize(0, 40))
        self.cmbSetores.setMaximumSize(QSize(16777215, 40))
        self.cmbSetores.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbSetores.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fff, stop:1 #f2f2f2);\n"
"	font: 12pt \"Calibri\";\n"
"	color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/img/arrow.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"	border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border: 1px solid rgba(0, 0, 0, 10%);\n"
"	padding: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fff, stop:1 #f2f2f2);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView::item {\n"
"	padding-left: 10px;\n"
"	background-color: transparent;\n"
"	color: black;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
"	background-color: qlineargradient(x1:0"
                        ", y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"}\n"
"\n"
"QComboBox QListView::item:selected {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"}")

        self.gridLayout.addWidget(self.cmbSetores, 5, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 10, 40, 20)
        self.lblTopInstrucoes = QLabel(self.frame_2)
        self.lblTopInstrucoes.setObjectName(u"lblTopInstrucoes")
        self.lblTopInstrucoes.setMaximumSize(QSize(16777215, 25))
        self.lblTopInstrucoes.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Calibri\";\n"
"	background-color: rgb(224, 224, 224);\n"
"	color: #fff;\n"
"	border-top-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"}")
        self.lblTopInstrucoes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblTopInstrucoes)

        self.lblInstrucoes = QLabel(self.frame_2)
        self.lblInstrucoes.setObjectName(u"lblInstrucoes")
        self.lblInstrucoes.setCursor(QCursor(Qt.OpenHandCursor))
        self.lblInstrucoes.setStyleSheet(u"QLabel {\n"
"	padding: 15px;\n"
"	font: 12pt \"Calibri\";\n"
"	background-color: rgb(242, 242, 242);\n"
"	border-bottom-right-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.lblInstrucoes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblInstrucoes.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lblInstrucoes)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnIniciar = QPushButton(self.frame_3)
        self.btnIniciar.setObjectName(u"btnIniciar")
        self.btnIniciar.setMinimumSize(QSize(300, 40))
        self.btnIniciar.setMaximumSize(QSize(40, 16777215))
        self.btnIniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnIniciar.setStyleSheet(u"QPushButton {\n"
"	background-color: #853375;\n"
"	color: #fff;\n"
"	border: 1px solid transparent;\n"
"	border-radius: 10px;\n"
"	font: 700 12pt \"Calibri\";\n"
"	padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #A94C7D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(169, 76, 125, 80%);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btnIniciar)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.logoNeo.setText("")
        self.lblColaborador.setText(QCoreApplication.translate("Dialog", u"COLABORADOR:", None))
        self.txtColaborador.setText("")
        self.txtColaborador.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite seu nome..", None))
        self.lblMatricula.setText(QCoreApplication.translate("Dialog", u"MATR\u00cdCULA:", None))
        self.txtMatricula.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite sua matr\u00edcula..", None))
        self.lblSetor.setText(QCoreApplication.translate("Dialog", u"SETOR:", None))
        self.cmbSetores.setPlaceholderText(QCoreApplication.translate("Dialog", u"Selecione uma op\u00e7\u00e3o..", None))
        self.lblTopInstrucoes.setText(QCoreApplication.translate("Dialog", u"Instru\u00e7\u00f5es Gerais", None))
        self.lblInstrucoes.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>N\u00e3o esque\u00e7a de preencher o nome, a matr\u00edcula e o setor.</p><p>As quest\u00f5es para a avalia\u00e7\u00e3o s\u00e3o exemplos da rotina di\u00e1ria no setor de modo geral.</p><p>O colaborador deve selecionar somente uma \u00fanica op\u00e7\u00e3o correta.</p><p>O colaborador n\u00e3o deve em hip\u00f3tese alguma, deixar uma pergunta sem resposta.</p><p>N\u00e3o se deve tirar fotos do teste ou utilizar outro qualquer meio de consulta.</p></body></html>", None))
        self.btnIniciar.setText(QCoreApplication.translate("Dialog", u"INICIAR AVALIA\u00c7\u00c3O", None))
    # retranslateUi

