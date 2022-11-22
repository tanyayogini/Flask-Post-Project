from flask import Blueprint, render_template, request
from functions import search_posts
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf8")

# блюпринт для главной страницы
main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


# страница с результатами поиска по слову
@main_blueprint.route('/search')
def search_page():
    s = request.args['s']
    logging.info(f"Выполняется поиск по слову {s}")
    posts = search_posts(s)
    return render_template('post_list.html', posts=posts, s=s)
