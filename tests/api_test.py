import pytest
 
class TestApi:

    def test_api_get_posts(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        
    def test_api_get_post(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/api/post/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"