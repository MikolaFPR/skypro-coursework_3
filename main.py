from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import abort
import logging

import utils

from api.api import api

app = Flask(__name__)


# Регистрация блупринта с апи
app.register_blueprint(api)

#настройка логгера, чтобы системные уведомления были в консоли
log = logging.getLogger('werkzeug')
log.disabled = True

# Стартовая страница
@app.route('/', methods=["GET"])
def get_index():
    posts = utils.load_all_post_from_json()
    bookmarks = utils.get_count_bookmarks()

    return render_template('index.html', posts=posts, bookmarks=bookmarks)


# Страница с постом
@app.route('/posts/<int:post_id>', methods=["GET"])
def get_single_post(post_id):
    post = utils.get_post_by_pk(post_id)
    print(type(post))
    comments = utils.get_comments_by_post_id(post_id)
    coms_count = f"{len(comments)} {utils.get_declination(len(comments))}"

    return render_template('post.html', post=post, comments=comments, total_comments=coms_count)


# Страница с результатом поиска по ключевому слову
@app.route('/search', methods=["GET"])
def search_posts():
    if "s" not in request.args:
        abort(404)

    query = request.args["s"]

    if query == "":
        return render_template('search.html', posts=[], posts_counts=0, query=query)

    posts = utils.search_for_posts(query)
    total_posts = len(posts)

    return render_template('search.html', posts_counts=total_posts, posts=posts, query=query)


# Страница с лентой конкретного пользователя
@app.route('/users/<string:username>', methods=["GET"])
def get_user_feed(username):
    posts = utils.get_posts_by_user(username)

    return render_template('user-feed.html', feed=posts, name=username)


# Страница с лентой по конкретному тегу
@app.route('/tag/<string:tag>', methods=["GET"])
def get_post_by_tags(tag):
    posts = utils.get_post_by_tag(tag)

    return render_template("tag.html", posts=posts, tag=tag)


# Добавление поста в закладки с редиректом на ту страницу, где было добавление
@app.route('/bookmarks/add/<int:post_id>')
def add_to_bookmark(post_id):
    redir = request.args.get("r", "/")

    utils.add_bookmark(post_id)

    return redirect(redir, code=302)


# Удаление поста из закладок с редиректом на ту страницу, где было добавление
@app.route('/bookmarks/remove/<int:post_id>')
def remove_from_bookmark(post_id):
    redir = request.args.get("r", "/")

    utils.remove_bookmark(post_id)

    return redirect(redir, code=302)


# обработчик ошибок
@app.errorhandler(400)
def handle_bad_request(_):
    return "Bad request!", 400


@app.errorhandler(404)
def handle_not_found(_):
    return "Page not found!", 404


@app.errorhandler(500)
def handle_server_error(_):
    return "Server error", 500


# Страница с отображением всех закладок
@app.route("/bookmarks", methods=["GET"])
def get_page_with_bookmarks():
    posts = utils.get_posts_with_bookmark()

    return render_template("bookmarks.html", bookmarks=posts)


if __name__ == "__main__":
    app.run()
