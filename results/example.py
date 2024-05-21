from lists import LISTA_EXEMPLO

for valor in LISTA_EXEMPLO:
    img_question = valor['IMAGEM_PERGUNTA']
    list_imgs = img_question.split(';')
    # print(list_imgs)
    # print(len(list_imgs))
    for i, valor in enumerate(list_imgs):
        print(i)
        print(valor)
        print('*' * 10)
    print('=' * 50)
