import sys
from PySide6.QtWidgets import (
    QApplication, QMessageBox, QDialog
)
from PySide6.QtGui import QIcon, QIntValidator
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from questions import Questionario
from ui.login_ui import Ui_Dialog
from connection import connectionDB


class LoginWindow(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(
            'Preencha seus dados para inicar a avaliação - '
            'Teste de Nivelamento'
        )
        icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(icon)

        setores = connectionDB().requestSector()
        for setor in setores:
            self.cmbSetores.addItem(setor)

        int_validator = QIntValidator(self)
        self.txtMatricula.setValidator(int_validator)

        self.btnIniciar.clicked.connect(self.login)

    def login(self):
        self.nome = self.txtColaborador.text()
        self.matricula = self.txtMatricula.text()
        self.setor = self.cmbSetores.currentText()

        # Exemplo de verificação de campos vazios
        if not self.nome or not self.matricula or not self.setor:
            QMessageBox.warning(
                self, 'Aviso', 'Por favor, preencha todos os campos.'
            )
            return

        # Após o login bem-sucedido, feche e abra a janela principal
        self.accept()


def check_questions(setor: str):
    questions = Questionario().questions(setor)
    if not questions:
        msg = QMessageBox()
        msg.setText(
            'Desculpe o número de perguntas não é o '
            'suficiente para iniciar a prova.'
        )
        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        msg.setDefaultButton(QMessageBox.StandardButton.Close)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle('Teste de Nivelamento - Erro ao iniciar')
        icon = QIcon(str(WINDOW_ICON_PATH))
        msg.setWindowIcon(icon)
        msg.exec()
        return False
    return questions


if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    if login_window.exec() == QDialog.Accepted:
        nome = login_window.txtColaborador.text()
        matricula = int(login_window.txtMatricula.text())
        setor = login_window.cmbSetores.currentText()
        dict_dados = {
            'Colaborador': nome,
            'Matricula': matricula,
            'Setor': setor
        }
        check = check_questions(dict_dados['Setor'])
        if not check:
            sys.exit()

        window = MainWindow(check, dict_dados)
        icon = QIcon(str(WINDOW_ICON_PATH))
        window.setWindowIcon(icon)
        app.setWindowIcon(icon)

        window.show()
        app.exec()
