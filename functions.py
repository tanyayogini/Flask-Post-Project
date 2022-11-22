import json
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf8")


def load_json():
    """Загружает посты из файла в список. Если файл
    не найден или в неподходящем формате, происходит логирование ошибки и
    возвращается пустой список"""

    try:
        with open("posts.json", 'r', encoding='utf8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Ошибка при загрузке файла: {e}")
        return []


def search_posts(search_word):
    """Принимает слово для поиска, отдает список с постами, где встречается это слово"""

    posts_with_word = []
    posts = load_json()
    for post in posts:
        if search_word.lower() in post['content'].lower():
            posts_with_word.append(post)

    return posts_with_word


def add_post_to_file(new_post):
    """Принимает новый пост в формате словаря, записывает его в файл с постами"""
    posts = load_json()
    posts.append(new_post)
    with open("posts.json", 'w', encoding='utf8') as f:
        json.dump(posts, f)
