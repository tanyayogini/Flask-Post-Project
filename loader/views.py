from flask import Blueprint, request, render_template
from functions import add_post_to_file
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf8")

# создаем блюпринт для загрузки нового поста
loader_blueprint = Blueprint('loader_blueprint', __name__)


# форма загрузка поста
@loader_blueprint.route('/post/')
def load_page():
    return render_template('post_form.html')


# загрузка поста, проверка на наличие текста и файла, проверка, является ли файл картинкой
# сохранение файла, добавление поста в файл с постами и показ загруженного поста
@loader_blueprint.route('/post/', methods=['POST'])
def add_post():
    content = request.form['content']
    picture = request.files.get('picture')

    if not content or not picture:
        return "Ошибка загрузки"

    picture_filename = picture.filename
    file_type = picture_filename.split(".")[-1]
    if file_type not in ['png', 'jpeg']:
        logging.info(f"Загруженный файл {picture_filename} не картинка")
        return "Это не изображение"

    picture.save(f"./uploads/{picture_filename}")
    picture_path = f"/uploads/{picture_filename}"

    new_post = {
                    "pic": picture_path,
                    "content": content
                }
    add_post_to_file(new_post)

    return render_template('post_uploaded.html', content=content, picture_path=picture_path)
