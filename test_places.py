import pytest
import geopy

from base import BaseMethod

url = "https://demo.maps.mail.ru"


class TestPlaceInterest:
    """Документация https://help.mail.ru/maps/search-and-geocoding/places/v3"""

    @pytest.mark.parametrize('value', ['metro', 'museum', 'magazine', 'theatre'])
    def test_connection(self, value):
        response = BaseMethod(url).get_places_of_interests(q=value)
        assert response.status_code == 200, 'Есть проблемы с кодом ответа от сервера'
        assert response.headers['Content-Type'] == 'application/json; charset=UTF-8', 'Формат не json'

    @pytest.mark.parametrize('empty', ["", None])
    def test_q_is_empty(self, empty):
        response = BaseMethod(url).get_places_of_interests(q=empty)
        assert response.json()['error'] == 'Empty query'

    def test_q_is_integer(self):
        response = BaseMethod(url).get_places_of_interests(q=-1)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    def test_with_all_fields(self):
        fields = {'fields': 'name,place_details,address_details,address,pin,bbox,geometry,type'}
        response = BaseMethod(url).get_places_of_interests(q='metro', **fields)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    @pytest.mark.parametrize('field_name', ['name', 'place_details', 'address_detailse', 'address',
                                            'pin', 'bbox', 'geometry', 'type'])
    def test_with_one_fields(self, field_name):
        fields = {'fields': field_name}
        response = BaseMethod(url).get_places_of_interests(q='metro', **fields)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    @pytest.mark.parametrize('type', ['metro', 'hotel'])
    def test_with_one_type(self, type):
        types = {'types': type}
        response = BaseMethod(url).get_places_of_interests(q='Sokolniki', **types)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    @pytest.mark.parametrize('lang', ['ru', 'en', 'de', 'it', 'es'])
    def test_lang(self, lang):
        languages = {'lang': lang}
        response = BaseMethod(url).get_places_of_interests(q='Sokolniki', **languages)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    def test_location(self):
        location = {'location': "55.66,37.53"}
        response = BaseMethod(url).get_places_of_interests(q='metro', **location)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    def test_radius_with_location(self):
        radius_with_location = {'location': "55.66,37.53", 'radius': 500}
        response = BaseMethod(url).get_places_of_interests(q='metro', **radius_with_location)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    def test_radius_without_location(self):
        radius_without_location = {'location': None, 'radius': 500}
        response = BaseMethod(url).get_places_of_interests(q='metro', **radius_without_location)
        assert response.status_code == 400, "Есть ошибка с кодом ответа от сервера"

    @pytest.mark.parametrize('limit', list(range(1, 101)))
    def test_limit(self, limit):
        limit = {'limit': limit}
        response = BaseMethod(url).get_places_of_interests(q='metro', **limit)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"

    def test_limit_more_100(self):
        limit = {'limit': 101}
        response = BaseMethod(url).get_places_of_interests(q='metro', **limit)
        assert response.status_code == 400, "Есть ошибка с кодом ответа от сервера"

    def test_with_full_params(self):
        full_params = {'limit': 10, 'lang': 'ru', 'type': 'metro',
                       'location': '55.33, 34.56', 'radius': 100,
                       'fields': 'name,place_details,address_details,address,pin,bbox,geometry,type'}
        response = BaseMethod(url).get_places_of_interests(q='Kiev', **full_params)
        assert response.status_code == 200, "Есть ошибка с кодом ответа от сервера"