import random
from connection import connectionDB
from results.charts import BarChart


class Questionario():
    def __init__(self) -> None:
        self.conn = connectionDB()
        self.setores = self.conn.requestSector()

    def questions(self, refer_setor: str):
        self.setor = refer_setor
        list_question = []
        if refer_setor not in self.setores:
            print('O setor não existe no bando de dados.')
            return

        responseQuestions = self.conn.resultQuestion(refer_setor)
        responseCategories = self.conn.categoriesQuestion(refer_setor)
        if not responseCategories:
            print(f'Não informado categorias para o setor "{refer_setor}".')
            return

        total_categorias = len(responseCategories)
        qtde_pergunta = self.conn.qtdePerguntas(refer_setor)
        media = int(qtde_pergunta / total_categorias)

        if qtde_pergunta > len(responseQuestions):
            return

        dic_categoria = {}
        for categoria in responseCategories:
            for pergunta in responseQuestions:
                if pergunta['CATEGORIA_PERGUNTA'].upper() == categoria.upper():
                    if categoria not in dic_categoria:
                        dic_categoria[categoria] = [pergunta]
                    else:
                        dic_categoria[categoria].append(pergunta)

        list_perguntas = []
        for catg in dic_categoria:
            list_dinamic = dic_categoria[catg]
            random.shuffle(list_dinamic)
            for questao in list_dinamic[:media]:
                list_perguntas.append(questao)

        list_question = list_perguntas[:]
        random.shuffle(list_question)
        return list_question

    def startTest(self, setor):
        questoes = self.questions(setor)
        if not questoes:
            print('Desculpe, mas o número de questões não é o suficiente.')
            return

        self.varNome = 'Luiz Cheva'
        self.matricula = 5177
        varAcerto = 0
        varErro = 0
        total_perguntas = len(questoes)
        print('#' * 30, f'TESTE DE NIVELAMENTO - {self.varNome}', '#' * 30)
        print()
        list_catg = []
        for num, questao in enumerate(questoes):
            descricao = questao['PERGUNTA']
            img = questao['IMAGEM_PERGUNTA']
            ctg = questao['CATEGORIA_PERGUNTA']
            alternativas = questao['ALTERNATIVAS'].split(';')
            random.shuffle(alternativas)
            print(f'{num + 1} - {descricao}')
            print(img)
            list_catg.append(ctg)
            list_alternativas = {}
            for indice, alternativa in enumerate(alternativas):
                op = chr(indice + 65)
                txt_breve = alternativa.strip()
                list_alternativas[op] = txt_breve
                print(
                    f'{op.upper()}) {txt_breve}'
                )
            resposta_correta = questao['RESPOSTA_CORRETA']
            while True:
                resposta = input(
                    'Digite a opção que possui a resposta correta: '
                ).upper()
                if resposta not in list_alternativas:
                    print('Desculpe, opção inválida!')
                else:
                    break
            print(list_alternativas[resposta])
            print(resposta_correta)
            if list_alternativas[resposta] == resposta_correta:
                varAcerto += 1
                questao['STATUS'] = True
            else:
                varErro += 1
                questao['STATUS'] = False
            print('-' * 30)

        print()
        print('#' * 30, 'FINALIZANDO O TESTE...', '#' * 30)
        print('Resultado do teste:')
        print(f'Colaborador: {self.varNome}')
        print(f'Total de acertos: {varAcerto}')
        print(f'Total de erros: {varErro}')

        media = varAcerto / total_perguntas * 100
        vMedia = round(media)
        if vMedia >= 50:
            print('PARABÉNS - VOCÊ FOI APROVADO')
            print(f'Você acertou {media:.0f}% da prova.')
        else:
            print('QUE PENA - VOCÊ FOI REPROVADO')
            print(f'Você acertou {media:.0f}% da prova.')
        print()
        return questoes


if __name__ == '__main__':
    app = Questionario()
    questoes = app.startTest('CQ_USI')
    graficos = BarChart(
        questoes,
        app.varNome,
        app.matricula,
        app.setor
    )
    # grafico
    # print(len(questoes))
    # if questoes:
    #     list_id = []
    #     list_setor = []
    #     for num, questao in enumerate(questoes):
    #         descricao = questao['PERGUNTA']
    #         alternativas = questao['ALTERNATIVAS'].split(';')
    #         print(f'{num + 1} - {descricao}')
    #         list_ops = {}
    #         for num, alternativa in enumerate(alternativas):
    #             op = chr(num + 65).upper()
    #             print(f'{op}) {alternativa.strip()}')
    #             list_ops[op] = alternativa.strip()
    #         print(list_ops)
    #         while True:
    #             resposta = input(
    #                     'Digite a opção que possui a resposta certa: '
    #                 ).upper()
    #             print(True if resposta in list_ops else False)
    #             if resposta in list_ops:
    #                 break
    #             else:
    #                 print('Desculpe opção inválida.')
    #         print(list_ops[resposta])
    #         list_id.append(questao['ID'])
    #         list_setor.append(questao['SETOR'])
    #         print('-' * 50)
    #     print(list_id)
    #     print(f'Total de perguntas: {len(questoes)}')
    # else:
    #     print('Número de questões não é o suficiente.')
