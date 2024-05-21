import os
import datetime
import random
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout,
    QFrame, QSizePolicy, QSpacerItem, QHBoxLayout,
    QRadioButton, QMessageBox, QPushButton
)
from PySide6.QtCore import QTimer, QDateTime, Qt
from PySide6.QtGui import QPixmap
from ui.main_ui import Ui_MainWindow
from save import results


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, lista_pergunta: list, dict_dados: dict) -> None:
        super().__init__()
        self.nome = dict_dados['Colaborador']
        self.matricula = dict_dados['Matricula']
        self.setor = dict_dados['Setor']
        self.btnFinalizar = None
        self.confirm_close = True
        self.setupUi(self)
        self.list_question = lista_pergunta
        self.slots()
        self.carregaBarra()
        self.carregaPaginas()

    def slots(self):
        self.btnAnterior.setVisible(False)
        self.btnProximo.clicked.connect(self.nextPage)
        self.btnAnterior.clicked.connect(self.previousPage)

    def carregaBarra(self):
        agora = datetime.datetime.now()
        agora = agora.strftime("%d/%m/%Y")
        user = os.environ.get('USERNAME')
        lbl1 = QLabel(agora)
        lbl1.setStyleSheet('margin-left: 10px; margin-right: 10px;')
        lbl2 = QLabel(f'Colaborador: {user}')
        lbl2.setStyleSheet('margin-left: 10px; margin-right: 10px;')
        self.lbl3 = QLabel()
        self.lbl3.setStyleSheet('margin-left: 10px; margin-right: 10px;')

        self.statusbar.setStyleSheet(
            'border: 0; background-color: #FFFFFF; color: black;'
        )
        self.statusbar.addWidget(lbl1)
        self.statusbar.reformat()
        self.statusbar.addWidget(lbl2)

        timer = QTimer(self)
        timer.timeout.connect(self.updateTimer)
        self.start_time = QDateTime.currentDateTime()
        timer.start(1000)
        self.statusbar.addWidget(self.lbl3)

    def updateTimer(self):
        current_time = QDateTime.currentDateTime()
        elapsed = self.start_time.secsTo(current_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.lbl3.setText(f"Tempo decorrido: {formatted_time}")

    def layout(self, num: int, questao: str, image: str, alternativas: str):
        page = QWidget()  # Creating a page
        # -> Creating a question frame <-
        area_pergunta = QFrame()
        area_pergunta.setStyleSheet(
            'background: transparent;'
            'border: 1px solid rgba(255,255,255, 100);'
        )
        area_pergunta.setMinimumSize(0, 410)
        area_pergunta.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        topPergunta = QWidget()
        labelQuestion = QLabel()
        wdgImages = QWidget()

        topPergunta.setStyleSheet('border: none;')
        labelQuestion.setStyleSheet('border: none;')
        wdgImages.setStyleSheet('border: none;')

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(topPergunta)
        verticalLayout.addWidget(labelQuestion)
        verticalLayout.addWidget(wdgImages)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(0)

        area_pergunta.setLayout(verticalLayout)

        referPergunta = QLabel()
        referPergunta.setMaximumWidth(350)
        referPergunta.setMinimumWidth(350)
        numQuestao = num + 1
        referPergunta.setText(f'PERGUNTA {numQuestao:02}')
        referPergunta.setStyleSheet(
            'border: none;'
            'background-color: rgba(255, 255, 255, 100);'
            'border-bottom-right-radius: 10px;'
            'padding-left: 10px;'
            'color: white;'
            'font-family: Calibri;'
            'font-size: 16pt;'
            'font-weight: 700;'
        )
        referPergunta.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        hSpacer = QSpacerItem(
            725, 20, QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(referPergunta)
        horizontalLayout.addItem(hSpacer)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(0)
        topPergunta.setLayout(horizontalLayout)
        topPergunta.setMaximumHeight(30)
        topPergunta.setMinimumHeight(30)

        labelQuestion.setText(
            questao
        )
        labelQuestion.setMaximumHeight(40)
        labelQuestion.setStyleSheet(
            'background-color:transparent;'
            'border: none;'
            'padding-left: 10px;'
            'font-family: Calibri;'
            'color: rgb(236, 197, 209);'
            'font-size: 12pt;'
        )

        list_image = image.split(';')
        horizontalLayout_2 = QHBoxLayout()
        horizontalLayout_2.setSpacing(5)
        horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        wdgImages.setLayout(horizontalLayout_2)
        for img in list_image:
            self.image_label = QLabel()
            self.image_label.setStyleSheet('background-color: transparent;')
            horizontalLayout_2.addWidget(
                self.image_label, 0, Qt.AlignmentFlag.AlignHCenter
            )
            self.set_image(img)

        # -> Creating a options frame <-
        area_alternativas = QFrame()
        area_alternativas.setStyleSheet(
            'background: transparent;'
            'border: 1px solid rgba(255,255,255, 100);'
        )

        area_alternativas.setMinimumSize(0, 215)
        topAlternativa = QWidget()
        self.wdgAlternativa = QWidget()
        topAlternativa.setStyleSheet('border: none;')
        self.wdgAlternativa.setStyleSheet('border: none;')

        verticalLayout_1 = QVBoxLayout()
        verticalLayout_1.addWidget(topAlternativa)
        verticalLayout_1.addWidget(self.wdgAlternativa)
        verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        verticalLayout_1.setSpacing(0)

        area_alternativas.setLayout(verticalLayout_1)

        referAlternativa = QLabel()
        referAlternativa.setMaximumWidth(350)
        referAlternativa.setMinimumWidth(350)
        referAlternativa.setText('ALTERNATIVAS')
        referAlternativa.setStyleSheet(
            'border: none;'
            'background-color: rgba(255, 255, 255, 100);'
            'border-bottom-right-radius: 10px;'
            'padding-left: 10px;'
            'color: white;'
            'font-family: Calibri;'
            'font-size: 16pt;'
            'font-weight: 700;'
        )
        referAlternativa.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        hSpacer_2 = QSpacerItem(
            725, 20, QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )

        horizontalLayout_1 = QHBoxLayout()
        horizontalLayout_1.addWidget(referAlternativa)
        horizontalLayout_1.addItem(hSpacer_2)
        horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_1.setSpacing(0)
        topAlternativa.setLayout(horizontalLayout_1)
        topAlternativa.setMaximumHeight(30)
        topAlternativa.setMinimumHeight(30)

        list_alternativas = alternativas.split(';')
        self.verticalLayout_2 = QVBoxLayout()
        random.shuffle(list_alternativas)
        for i, alternativa in enumerate(list_alternativas):
            opt = QRadioButton()
            opt.setObjectName(f'opt{i}')
            opt.setText(alternativa.strip())
            opt.setCursor(Qt.CursorShape.PointingHandCursor)
            opt.setStyleSheet(
                "QRadioButton {"
                "color: rgb(236, 197, 209);"
                "padding: 5px;"
                "font: 12pt 'Calibri';"
                "}"
                "QRadioButton:hover {"
                "color: #FFFFFF;"
                "}"
                "QRadioButton:checked {"
                "color: #FFFFFF;"
                "}"
                "QRadioButton::indicator {"
                "width: 15px;"
                "height: 15px;"
                "border-radius: 5px;"
                "border: 1px solid rgb(236, 197, 209);"
                "margin-right: 20px;"
                "}"
                "QRadioButton::indicator:checked {"
                "background-color: rgb(236, 197, 209);"
                "}"
                "QRadioButton::indicator:unchecked {"
                "background-color: transparent;"
                "}"
                "QRadioButton::indicator:unchecked:hover {"
                "border: 1px solid #FFFFFF;"
                "}"
            )
            self.verticalLayout_2.addWidget(opt)

        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setSpacing(5)
        self.wdgAlternativa.setLayout(self.verticalLayout_2)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.addWidget(area_pergunta)
        layout.addWidget(area_alternativas)
        page.setLayout(layout)
        self.wdgPages.addWidget(page)

    def carregaPaginas(self):
        catg = self.list_question[0]
        categoria = catg['CATEGORIA_PERGUNTA']
        self.show_catg = QLabel(f'Categoria da Pergunta: {categoria}')
        self.show_catg.setStyleSheet('margin-left: 10px; margin-right: 10px;')
        self.statusbar.addWidget(self.show_catg)
        for num, valr in enumerate(self.list_question):
            self.layout(
                num, valr['PERGUNTA'],
                valr['IMAGEM_PERGUNTA'],
                valr['ALTERNATIVAS']
            )

        page_del = self.wdgPages.widget(0)
        self.wdgPages.removeWidget(page_del)
        self.wdgPages.setCurrentIndex(0)
        self.current_page = self.wdgPages.currentIndex()
        if self.current_page == 0:
            self.btnAnterior.setVisible(False)

    def nextPage(self):
        isChecked = self.isRadioButtonSelected()
        if not isChecked:
            QMessageBox.warning(
                self,
                "Aviso",
                "Por favor, selecione pelo menos uma opção antes de avançar."
            )
            return
        self.wdgPages.setCurrentIndex(self.current_page + 1)
        self.current_page = self.wdgPages.currentIndex()
        if self.current_page > 0:
            self.btnAnterior.setVisible(True)

        if self.current_page == self.wdgPages.count() - 1:
            if self.btnFinalizar is None:
                self.btnProximo.setVisible(False)
                self.createBtnFinalizar()

        for num, valor in enumerate(self.list_question):
            if self.current_page == num:
                catg = valor['CATEGORIA_PERGUNTA']
                self.show_catg.setText(f'Categoria da Pergunta: {catg}')

    def previousPage(self):
        self.wdgPages.setCurrentIndex(self.current_page - 1)
        self.current_page = self.wdgPages.currentIndex()
        if self.current_page == 0:
            self.btnAnterior.setVisible(False)

        if self.current_page < self.wdgPages.count() - 1:
            if self.btnFinalizar is not None:
                self.horizontalLayout_3.removeWidget(self.btnFinalizar)
                self.btnFinalizar.deleteLater()
                self.btnFinalizar = None
                self.btnProximo.setVisible(True)

        for num, valor in enumerate(self.list_question):
            if self.current_page == num:
                catg = valor['CATEGORIA_PERGUNTA']
                self.show_catg.setText(f'Categoria da Pergunta: {catg}')

    def set_image(self, path):
        # Carregando a imagem
        image = QPixmap(path)

        # Atualizando a imagem na QLabel
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(image)

    def closeEvent(self, event):
        if self.confirm_close:
            reply = QMessageBox.question(
                self,
                'Atenção',
                'Tem certeza que deseja sair?\n'
                'Isso não salvará as informações!',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def createBtnFinalizar(self):
        self.btnFinalizar = QPushButton('Finalizar avaliação')
        self.btnFinalizar.setStyleSheet(
            "QPushButton {"
            "background-color: transparent;"
            "border: 1px solid rgba(255, 255, 255, 240);"
            "border-top-left-radius: 10px;"
            "border-bottom-right-radius: 10px;"
            "color: white;"
            "}"
            "QPushButton:hover {"
            "background-color: rgba(255, 255, 255, 240);"
            "color: black;"
            "}"
            "QPushButton:pressed {"
            "background-color: rgba(255, 255, 255, 200);"
            "color: black;"
            "}"
        )
        self.btnFinalizar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btnFinalizar.setMinimumHeight(30)
        self.btnFinalizar.setMaximumHeight(30)
        self.btnFinalizar.setMaximumWidth(150)
        self.btnFinalizar.setMinimumWidth(150)
        self.save_report = results(self, self.list_question)
        self.btnFinalizar.clicked.connect(self.save_report.report)
        self.horizontalLayout_3.addWidget(self.btnFinalizar)

    def isRadioButtonSelected(self):
        rd = self.wdgPages.widget(self.wdgPages.currentIndex()).findChildren(
            QRadioButton
        )
        for rdBtn in rd:
            if isinstance(rdBtn, QRadioButton):
                if rdBtn.isChecked():
                    return True

        return False
