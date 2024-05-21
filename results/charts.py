import matplotlib.pyplot as plt
import os


class BarChart:
    def __init__(
            self, list_question: list, nome: str, matricula: int, setor: str
    ) -> None:
        self.chart = plt
        self.list_x = []
        self.list_y = []
        self.nome = nome
        self.matricula = matricula
        self.setor = setor
        self.total_perguntas = len(list_question)
        self.results = self.calculaResultado(list_question)
        if self.results:
            self.createBarCart(
                self.list_x,
                self.list_y
            )
            self.createBarHCart(
                self.list_x,
                self.list_y
            )
            self.createPieChart(
                self.list_y,
                self.list_x
            )
        else:
            print('Desculpe resultados inválidos')
            return

    def calculaResultado(self, lista: list):
        if not lista:
            return
        self.list_catg = []
        dict_results = {}
        for response in lista:
            categoria = response['CATEGORIA_PERGUNTA']
            if categoria not in self.list_catg:
                self.list_catg.append(categoria)

        for catg in self.list_catg:
            varAcerto = 0
            varErro = 0
            for resp in lista:
                if resp['CATEGORIA_PERGUNTA'] == catg:
                    if resp['STATUS']:
                        varAcerto += 1
                    else:
                        varErro += 1
            dict_results[catg] = [varAcerto, varErro]

        for indice, valor in dict_results.items():
            self.list_x.append(indice)
            self.list_y.append(valor[0])
        return True

    def createBarCart(self, list_x: list, list_y: list):
        # Dados
        x = list_x
        y = list_y

        # Criar o gráfico
        # plt.barh(x, y, color='#853375',  label='')
        _, ax1 = plt.subplots(figsize=(7, 3), layout='constrained')
        ax1.bar(
            x, y, color='#853375', label='Qtde. Acertos',
            align='center', width=0.5
        )

        for tick in plt.gca().get_xticklabels():
            tick.set_rotation(15)

        # Adicionar rótulos e título
        plt.xlabel('Nome da categoria')
        plt.ylabel('Total de acertos')
        plt.title('Avaliação por categoria', pad=20)
        # plt.gcf().autofmt_xdate()
        # plt.subplots_adjust(bottom=0.3, left=0.15)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.legend()

        # for i in range(len(x)):
        #     plt.text(y[i] + 0.05, x[i], str(y[i]), ha='left', va='center')

        for i in range(len(x)):
            plt.text(x[i], y[i] + 0.05, str(y[i]), ha='center', va='bottom')

        # Exibir o gráfico
        caminho = (
            f'results/graficos/{self.nome}_{self.matricula}/{self.setor}/'
            'barGraph.png'
        )
        diretorio = os.path.dirname(caminho)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        plt.savefig(caminho)
        # plt.savefig('graph.pdf')

    def createBarHCart(self, list_x: list, list_y: list):
        perguntas_p_categorias = self.total_perguntas / len(self.list_catg)
        # Dados
        x = list_x
        y = list_y
        porcentagem = [
            (valor / perguntas_p_categorias) * 100 for valor in y
        ]

        # Criar o gráfico
        _, ax2 = plt.subplots(figsize=(7, 3), layout='constrained')
        ax2.barh(x, porcentagem, color='#305496', align='center', height=0.5)

        for tick in plt.gca().get_yticklabels():
            tick.set_rotation(25)

        # Adicionar rótulos e título
        plt.xlabel("% de acertos")
        plt.ylabel('Nome da categoria')
        plt.title('% Geral de acertos')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)

        for i in range(len(x)):
            plt.text(
                porcentagem[i] + 1, x[i], f'{porcentagem[i]:.0f}%',
                ha='left', va='center'
            )

        # Exibir o gráfico
        caminho = (
            f'results/graficos/{self.nome}_{self.matricula}/{self.setor}/'
            'barHGraph.png'
        )
        diretorio = os.path.dirname(caminho)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        plt.savefig(caminho)
        # plt.savefig('graph.pdf')

    def createPieChart(self, list_y: list, list_x: list = None):
        # Dados
        x = 'Acerto', 'Erro'
        y = list_y
        acertos = 0
        for soma in y:
            acertos += soma

        erros = self.total_perguntas - acertos
        perAcertos = round((acertos / self.total_perguntas) * 100, 0)
        perErros = round((erros / self.total_perguntas) * 100, 0)
        list_results = [perAcertos, perErros]
        size = 0.3

        _, ax2 = plt.subplots(figsize=(7, 3), layout='constrained')
        ax2.pie(
            list_results, autopct='%1.1f%%',
            pctdistance=1.5, wedgeprops=dict(width=size, edgecolor='w'),
            radius=0.85, colors=['#305496', '#C7C7C7'], explode=(0.03, 0),
            startangle=90
        )
        ax2.legend(labels=x)
        plt.title('% total de acertos')

        caminho = (
            f'results/graficos/{self.nome}_{self.matricula}/{self.setor}/'
            'pieGraph.png'
        )
        diretorio = os.path.dirname(caminho)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        plt.savefig(caminho)


if __name__ == '__main__':
    from lists import LISTA_EXEMPLO
    grafico = BarChart(
        LISTA_EXEMPLO,
        'Luiz Cheva',
        5177,
        'CQ_USI'
    )
