import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QProgressBar, QWidget
from docx import Document
from docx2pdf import convert
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversão de Documento para PDF")
        self.setGeometry(100, 100, 400, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.convert_button = QPushButton("Converter")
        self.convert_button.clicked.connect(self.convert_and_show_progress)
        self.layout.addWidget(self.convert_button)

    def add_list_to_doc(self, doc_path, items):
        # Criar um novo documento
        doc = Document()

        # Iterar sobre a lista e adicionar cada item como um novo parágrafo
        for item in items:
            doc.add_paragraph(str(item))

        # Salvar o documento
        doc.save(doc_path)

    def convert_docx_to_pdf(self, doc_path, pdf_dir):
        # Atualizar a barra de progresso
        self.progress_bar.setValue(20)
        QApplication.processEvents()

        # Certifique-se de que o diretório de saída existe
        os.makedirs(pdf_dir, exist_ok=True)

        # Converter .docx para .pdf
        convert(doc_path, pdf_dir)

        # Atualizar a barra de progresso
        self.progress_bar.setValue(100)
        QApplication.processEvents()

    def convert_and_show_progress(self):
        lista = ['Primeiro item', 'Segundo item', 'Terceiro item', 'Quarto item']
        caminho_doc = 'meu_documento.docx'
        pasta_pdf = 'pasta_para_pdfs'

        # Adicionar itens ao documento
        self.add_list_to_doc(caminho_doc, lista)

        # Configurar a barra de progresso
        self.progress_bar.setValue(0)
        QApplication.processEvents()

        # Converter o documento para PDF e mostrar progresso
        self.convert_docx_to_pdf(caminho_doc, pasta_pdf)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()