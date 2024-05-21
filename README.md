## Teste de Nivelamento - Neodent
Avaliação de nivelamento de colaboradores da Neodent.

## Sistema
PySide6
Sqlite3
QtDseginer

# Exportação
pyinstaller --name="Teste de Nivelamento" --noconfirm --noconsole --onefile --add-data='../ui/;ui/' --add-data='../img/;img/' --add-data='../db/;db/' --add-data='../results/;results/' --icon='../img/favicon.png' --clean --log-level=WARN --distpath='Teste de Nivelamento' --workpath='__localcode/build' --specpath='__localcode/' main.py