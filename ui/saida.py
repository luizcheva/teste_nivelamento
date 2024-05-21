# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saida.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
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
        self.side1 = QWidget(Dialog)
        self.side1.setObjectName(u"side1")
        self.side1.setMinimumSize(QSize(550, 0))
        self.side1.setMaximumSize(QSize(550, 16777215))
        self.side1.setStyleSheet(u"#side1 {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #A94C7D, stop:1 #853375);\n"
"	border-right: 2px solid rgba(255, 255, 255, 150);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.side1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.side1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 650))
        self.label.setMaximumSize(QSize(16777215, 650))
        self.label.setStyleSheet(u"QLabel {\n"
"	background-image: url(:/img/30anosNeo.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"")
        self.label.setPixmap(QPixmap(u":/img/implante_2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.side1)

        self.side2 = QWidget(Dialog)
        self.side2.setObjectName(u"side2")
        self.side2.setMinimumSize(QSize(470, 0))
        self.side2.setMaximumSize(QSize(470, 16777215))
        self.side2.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout = QVBoxLayout(self.side2)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 10)
        self.logoNeo = QLabel(self.side2)
        self.logoNeo.setObjectName(u"logoNeo")
        self.logoNeo.setMinimumSize(QSize(0, 80))
        self.logoNeo.setMaximumSize(QSize(16777215, 80))
        self.logoNeo.setStyleSheet(u"#logoNeo {\n"
"	margin: 20px 120px 20px;\n"
"}")
        self.logoNeo.setPixmap(QPixmap(u":/img/neodent-logo.png"))
        self.logoNeo.setScaledContents(True)

        self.verticalLayout.addWidget(self.logoNeo)

        self.frame_2 = QFrame(self.side2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 180, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setPixmap(QPixmap(u":/img/check.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 700 20pt \"Calibri\";\n"
"	color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(320, 150))
        self.groupBox.setMaximumSize(QSize(320, 150))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-radius: 5px;\n"
"	margin-top: 6px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-position: top center;\n"
"	padding-left: 100px;\n"
"	padding-right: 100px;\n"
"	padding-top: 2.5px;\n"
"	padding-bottom: 2.5px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"	font: 12pt \"Calibri\";\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tab_Results = QTableWidget(self.groupBox)
        if (self.tab_Results.columnCount() < 2):
            self.tab_Results.setColumnCount(2)
        if (self.tab_Results.rowCount() < 3):
            self.tab_Results.setRowCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_Results.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_Results.setItem(1, 0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_Results.setItem(2, 0, __qtablewidgetitem2)
        self.tab_Results.setObjectName(u"tab_Results")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_Results.sizePolicy().hasHeightForWidth())
        self.tab_Results.setSizePolicy(sizePolicy)
        self.tab_Results.setMinimumSize(QSize(300, 100))
        self.tab_Results.setMaximumSize(QSize(300, 100))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tab_Results.setFont(font)
        self.tab_Results.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tab_Results.setStyleSheet(u"QTableWidget  {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	gridline-color: #d1d1d1;\n"
"	selection-background-color: #a6a6a6;\n"
"	border-radius: 5px;\n"
"	font: 12pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	padding: 5px;\n"
"	border: none;\n"
"	color: black;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"	background-color: #A7A8A9;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: #636569;\n"
"	color: white;\n"
"}")
        self.tab_Results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_Results.setTabKeyNavigation(True)
        self.tab_Results.setProperty("showDropIndicator", True)
        self.tab_Results.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_Results.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_Results.setGridStyle(Qt.DotLine)
        self.tab_Results.setRowCount(3)
        self.tab_Results.setColumnCount(2)
        self.tab_Results.horizontalHeader().setVisible(False)
        self.tab_Results.horizontalHeader().setMinimumSectionSize(100)
        self.tab_Results.horizontalHeader().setDefaultSectionSize(150)
        self.tab_Results.verticalHeader().setVisible(False)
        self.tab_Results.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_3.addWidget(self.tab_Results)


        self.verticalLayout_2.addWidget(self.groupBox, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 179, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.side2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.logoNeo.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Resposta enviada com sucesso.", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Resultados da Avalia\u00e7\u00e3o", None))

        __sortingEnabled = self.tab_Results.isSortingEnabled()
        self.tab_Results.setSortingEnabled(False)
        ___qtablewidgetitem = self.tab_Results.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Total de Acertos", None));
        ___qtablewidgetitem1 = self.tab_Results.item(1, 0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Total de Erros", None));
        ___qtablewidgetitem2 = self.tab_Results.item(2, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"M\u00e9dia (%)", None));
        self.tab_Results.setSortingEnabled(__sortingEnabled)

    # retranslateUi

