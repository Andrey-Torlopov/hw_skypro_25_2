from app.modules.app_dao import AppDAO

import pytest

# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем
@pytest.fixture()
def dao():
    return AppDAO(
        './static/data/posts.json',
        './static/data/bookmarks.json',
        './static/data/comments.json')

# Задаем, какие ключи ожидаем получать у кандидата
keys_should_be = {"pk", "name", "position"}

class TestCandidateDao:

    def test_get_all(self, dao):
        """ Проверяему количество элементов в массиве"""
        posts = dao.load_posts()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"