from typing import TYPE_CHECKING
from PySide6.QtWidgets import (
    QMessageBox, QRadioButton, QDialog,
    QTableWidgetItem
)
from PySide6.QtGui import Qt
from ui.saida import Ui_Dialog
from results.charts import BarChart
from results.pdf import createPDF
if TYPE_CHECKING:
    from main_window import MainWindow


class results:
    def __init__(self, main: 'MainWindow', questions: list) -> None:
        self.main = main
        self.list_question = questions
        self.acertos = 0
        self.erros = 0

    def report(self):
        reply = QMessageBox.question(
            self.main,
            'Atenção',
            'Deseja finalizar a avaliação?\n '
            'Caso queria revisar as questões, clique em NÃO.',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes
        )

        if reply == QMessageBox.StandardButton.No:
            return

        list_reponse = []
        cPage = self.main.wdgPages.count()
        for i in range(cPage):
            opts = self.main.wdgPages.widget(i).findChildren(QRadioButton)
            for opt in opts:
                if isinstance(opt, QRadioButton):
                    if opt.isChecked():
                        list_reponse.append(opt.text())
                    else:
                        opt.setCheckable(False)

        resultados = self.calculaResultado(list_reponse)
        BarChart(
            resultados,
            self.main.nome,
            self.main.matricula,
            self.main.setor
        )
        self.main.confirm_close = False
        self.main.close()
        createPDF(
            self.main.nome,
            self.main.matricula,
            self.main.setor,
            resultados
        )
        self.success = SuccessWindow(
            self.acertos, self.erros, len(self.list_question)
        )
        self.success.exec()

    def calculaResultado(self, optSelected: list):
        list_results = self.list_question[:]
        for num, question in enumerate(list_results):
            resposta_correta = question['RESPOSTA_CORRETA']
            resposta_selecionada = optSelected[num]
            status = (
                True if resposta_selecionada == resposta_correta else False
            )
            if status:
                self.acertos += 1
            else:
                self.erros += 1

            question['STATUS'] = status
            print(question['PERGUNTA'])
            print(resposta_correta)
            print(resposta_selecionada)
            print(question['STATUS'])
            print()
            print('*' * 50)
            print()
        print(
            f'Total de Acertos: {self.acertos} X Total de erros: {self.erros}.'
        )

        return list_results


class SuccessWindow(QDialog, Ui_Dialog):
    def __init__(self, acertos: int, erros: int, qtdPerguntas: int) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Resultados da avaliação - Teste de Nivelamento')

        item_acertos = QTableWidgetItem(str(acertos))
        item_acertos.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item_erros = QTableWidgetItem(str(erros))
        item_erros.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        media = round(acertos / qtdPerguntas * 100, 0)
        item_media = QTableWidgetItem(f'{media:.0f}%')
        item_media.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab_Results.setItem(0, 1, item_acertos)
        self.tab_Results.setItem(1, 1, item_erros)
        self.tab_Results.setItem(2, 1, item_media)


if __name__ == '__main__':
    for x in range(10):
        print(x)
