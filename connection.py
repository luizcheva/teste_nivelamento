import sqlite3

TABLE_NAME = 'Questions'
DIR = (
    '\\\\straumann.com\\public\\br03\\pcoudir\\Controle de Qualidade\\'
    '01. 4400\\01. CQ Geral\\04. Pessoal\\01. Luiz Cheva\\'
    'bd_testenivelamento\\'
)


class connectionDB:
    def __init__(self) -> None:
        self.address = DIR + 'db.sqlite3'
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.address)
        except sqlite3.Error as e:
            print(f'Database unconnected. {e}')

    def closeDB(self):
        if self.conn:
            self.conn.close()
        else:
            print('Database already disconnected.')

    def executeQuery(self, Query=str):
        self.connect()
        if not self.conn:
            print('Error to execute any queries.')
            return
        cursor = self.conn.cursor()
        cursor.execute(Query)
        data = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data_table = [
            dict(zip(columns, row)) for row in data
        ]
        return data_table

    def resultQuestion(self, setor: str):
        query = f'SELECT * FROM {TABLE_NAME}'
        response = self.executeQuery(query)
        list_questions = []
        for questions in response:
            setores = str(questions['SETOR'])
            list_setores = setores.split(';')
            list_x = []
            for x in list_setores:
                if x:
                    list_x.append(x.strip())
            if setor in list_x:
                list_questions.append(questions)

        self.closeDB()
        return list_questions

    def requestSector(self):
        query = 'SELECT SETOR FROM Setores'
        response = self.executeQuery(query)
        list_setores = []
        for setor in response:
            list_setores.append(setor['SETOR'])
        self.closeDB()
        return list_setores

    def qtdePerguntas(self, setor: str):
        query = f'SELECT QTDE_PERGUNTAS FROM Setores WHERE SETOR = "{setor}";'
        response = self.executeQuery(query)
        self.closeDB()
        if len(response) == 0:
            return

        return response[0]['QTDE_PERGUNTAS']

    def categoriesQuestion(self, setor: str):
        query = 'SELECT * FROM Categorias'
        response = self.executeQuery(query)
        list_categoria = []
        for valor in response:
            categoria = valor['CATEGORIA']
            setores = valor['SETORES'].split(';')
            list_setores = []
            for vSetor in setores:
                list_setores.append(vSetor.strip())

            new_dict = {}
            new_dict['CATEGORIA'] = categoria
            new_dict['SETORES'] = list_setores
            if setor in new_dict['SETORES']:
                list_categoria.append(new_dict['CATEGORIA'])
        return list_categoria


if __name__ == '__main__':
    conexao = connectionDB()
    perguntas = conexao.resultQuestion('PROVA 04_CLEAR')
    categorias = conexao.categoriesQuestion('PROVA 04_CLEAR')
    print(perguntas)
    print(categorias)
