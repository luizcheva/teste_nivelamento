# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_backup.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 780)
        MainWindow.setMinimumSize(QSize(1100, 780))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 5)
        self.widgetLogo = QWidget(self.centralwidget)
        self.widgetLogo.setObjectName(u"widgetLogo")
        self.widgetLogo.setMinimumSize(QSize(0, 70))
        self.widgetLogo.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout = QHBoxLayout(self.widgetLogo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 0)
        self.imgLogo = QLabel(self.widgetLogo)
        self.imgLogo.setObjectName(u"imgLogo")
        self.imgLogo.setMinimumSize(QSize(150, 40))
        self.imgLogo.setMaximumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.imgLogo)

        self.horizontalSpacer = QSpacerItem(903, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widgetLogo)

        self.widgetQuestionario = QWidget(self.centralwidget)
        self.widgetQuestionario.setObjectName(u"widgetQuestionario")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetQuestionario)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.wdgPages = QStackedWidget(self.widgetQuestionario)
        self.wdgPages.setObjectName(u"wdgPages")
        self.wdgPages.setMinimumSize(QSize(0, 630))
        self.wdgPages.setStyleSheet(u"")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setStyleSheet(u"#page1 {\n"
"	background-color: transparent;\n"
"}")
        self.wdgPages.addWidget(self.page1)

        self.horizontalLayout_2.addWidget(self.wdgPages)


        self.verticalLayout.addWidget(self.widgetQuestionario)

        self.widgetBtns = QWidget(self.centralwidget)
        self.widgetBtns.setObjectName(u"widgetBtns")
        self.widgetBtns.setMinimumSize(QSize(0, 50))
        self.widgetBtns.setMaximumSize(QSize(16777215, 50))
        self.widgetBtns.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widgetBtns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnAnterior = QPushButton(self.widgetBtns)
        self.btnAnterior.setObjectName(u"btnAnterior")
        self.btnAnterior.setMinimumSize(QSize(150, 30))
        self.btnAnterior.setMaximumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        self.btnAnterior.setFont(font1)
        self.btnAnterior.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnterior.setStyleSheet(u"#btnAnterior {\n"
"	background-color: rgba(255, 255, 255, 240);\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"}\n"
"\n"
"#btnAnterior:hover {\n"
"	background-color: rgba(217, 225, 242, 255);\n"
"}\n"
"\n"
"#btnAnterior:pressed {\n"
"	background-color: rgba(217, 225, 242, 235);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnAnterior)

        self.horizontalSpacer_3 = QSpacerItem(387, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnProximo = QPushButton(self.widgetBtns)
        self.btnProximo.setObjectName(u"btnProximo")
        self.btnProximo.setMinimumSize(QSize(150, 30))
        self.btnProximo.setMaximumSize(QSize(150, 30))
        self.btnProximo.setFont(font1)
        self.btnProximo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnProximo.setStyleSheet(u"#btnProximo {\n"
"	background-color: rgba(255, 255, 255, 240);\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"}\n"
"\n"
"#btnProximo:hover {\n"
"	background-color: rgba(226, 239, 218, 255);\n"
"}\n"
"\n"
"#btnProximo:pressed {\n"
"	background-color: rgba(226, 239, 218, 235);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnProximo)


        self.verticalLayout.addWidget(self.widgetBtns)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Teste de Nivelamento", None))
        self.imgLogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/img/logo_neodent.png\"/></p></body></html>", None))
        self.btnAnterior.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.btnProximo.setText(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximo", None))
    # retranslateUi

