import os
from variables import FILES_DIR
from PIL import Image

DIR_IMG = FILES_DIR / 'image_resived'


def resize_image(image_path, new_width):
    # Carregue a imagem e redimensione-a usando Pillow
    nome_file, extensao = os.path.splitext(os.path.basename(image_path))
    img = Image.open(image_path)
    largura, altura = img.size
    new_height = round(altura * new_width / largura)

    img = img.resize(size=(new_width, new_height))

    # Salve a imagem redimensionada temporariamente
    if not os.path.exists(DIR_IMG):
        os.makedirs(DIR_IMG)

    NEW_IMAGE = DIR_IMG / f'{nome_file}_temp{extensao}'
    print(NEW_IMAGE)
    img.save(
        NEW_IMAGE,
    )

    # Insira a imagem redimensionada no QTextEdit
    html_img = f'<img src="{NEW_IMAGE}">'

    return html_img
