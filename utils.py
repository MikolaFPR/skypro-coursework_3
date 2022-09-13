import json
from post import Post
from comment import Comment


def load_all_post_from_json():
    """Переводим посты json в python"""
    posts = []

    bookmarks = json.load(open("data/bookmarks.json", "r"))

    with open("data/posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        for i in data:
            item = Post(i["poster_name"], i["poster_avatar"], i["pic"], i["content"], i["views_count"],
                        i["likes_count"], i["pk"], i["tags"])
            if item.pk in bookmarks:
                item.bookmark = True
            posts.append(item)

    return posts


def load_all_comments_from_json():
    """Переводим комменты json в python"""
    comments = []

    with open("data/comments.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        for i in data:
            item = Comment(i["post_id"], i["commenter_name"], i["comment"], i["pk"])
            comments.append(item)

    return comments


def get_posts_all():
    with open("data/posts.json", "r", encoding="utf-8") as f:
        return f.read()


def get_posts_by_user(user_name):
    """Возвращает все посты пользователя"""
    posts_by_user = []

    for i in load_all_post_from_json():
        if i.poster_name.lower() == user_name.lower():
            posts_by_user.append(i)

    return posts_by_user


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    comments_by_post = []

    for i in load_all_comments_from_json():
        if i.post_id == post_id:
            comments_by_post.append(i)

    return comments_by_post


def search_for_posts(query: str):
    """Возвращает список постов по ключевому слову"""
    result_of_search = []

    for i in load_all_post_from_json():
        if query.lower() in i.content.lower():
            result_of_search.append(i)

    return result_of_search


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    for i in load_all_post_from_json():
        if i.pk == pk:
            return i
    # return {}


def get_declination(num):
    """Возвращает правильное склонение слова"""
    w1 = 'комментариев'
    w2 = 'комментарий'
    w3 = 'комментария'

    if 10 <= num % 100 <= 20:
        return w1
    elif num % 10 == 1:
        return w2
    elif 2 <= num % 10 <= 4:
        return w3
    else:
        return w1


def get_post_by_tag(tag):
    """Возвращает посты по тегам"""
    posts_by_tag = []
    for i in load_all_post_from_json():
        if tag in i.tags:
            posts_by_tag.append(i)
    return posts_by_tag


def add_bookmark(post_id):
    """Добавление идентификатора поста в bookmarks.json"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if post_id not in data:
        data.append(post_id)
    with open("data/bookmarks.json", "w", encoding="utf-8") as f:
        json.dump(data, f)


def remove_bookmark(post_id):
    """Удаление идентификатора поста из bookmarks.json"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if post_id in data:
        data.remove(post_id)
    with open("data/bookmarks.json", "w", encoding="utf-8") as f:
        json.dump(data, f)


def get_count_bookmarks():
    """Возвращает число закладок"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        return len(data)


def get_posts_with_bookmark():
    """Возвращает посты, которые добавлены в закладки"""
    posts_with_bookmark = []

    for i in load_all_post_from_json():
        if i.bookmark:
            posts_with_bookmark.append(i)

    return posts_with_bookmark
