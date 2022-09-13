import pytest

import utils
from post import Post


# тесты функций
def test_load_all_post_from_json():
    assert len(utils.load_all_post_from_json()) != 0, 'Длина списка не должна равняться 0'
    assert type(utils.load_all_post_from_json()) == list, 'Тип возвращаемого файла должен быть list'


def test_load_all_comments_from_json():
    assert len(utils.load_all_comments_from_json()) != 0, 'Длина списка не должна равняться 0'
    assert type(utils.load_all_comments_from_json()) == list, 'Тип возвращаемого файла должен быть list'


def test_get_posts_by_user():
    assert len(utils.get_posts_by_user('leo')) == 2, 'Количество возвращаемых постов не совпадает с фактич. кол - вом'
    assert len(utils.get_posts_by_user('ololo')) == 0, 'Количество возвращаемых постов несуществующего юзера != 0'


def test_get_post_by_pk():
    assert utils.get_post_by_pk(-1) is None, 'Возвразается пост с несущестующим pk'


def test_get_comments_by_post_id():
    assert len(utils.get_comments_by_post_id(1)) == 4, 'возвращается неверное количество комментариев'
    assert len(utils.get_comments_by_post_id(-1)) == 0, 'возвращаются комментарии несуществующего поста'
    assert len(utils.get_comments_by_post_id(-1)) == 0, 'Тип возвращаемого файла должен быть list'


def test_search_for_post():
    assert type(utils.search_for_posts("я")) == list, 'возвращается не список'
