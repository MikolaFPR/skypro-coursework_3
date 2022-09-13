from flask import Blueprint, jsonify
import utils
import logging

api = Blueprint('api', __name__)

# Создание логгера
logging.basicConfig(level='INFO', format='%(asctime)s : [%(levelname)s] : %(message)s', filename='logs/api.log')

# Возвращает полный список постов в виде JSON-списка
@api.route('/api/posts', methods=["GET"])
def api_get_posts():
    logging.info('Запрос api/posts')
    posts = utils.get_posts_all()

    return posts


# Возвращает один пост в виде JSON-словаря
@api.route('/api/posts/<int:post_id>', methods=["GET"])
def api_get_post(post_id):
    logging.info(f'Запрос api/posts/{post_id}')
    post = utils.get_post_by_pk(post_id)

    return str(post)
