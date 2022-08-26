import requests

def test_api():
    response = requests.get("https://reqres.in/api/single_user")
    assert response.status_code == 200
    response_with_janet = requests.get("https://reqres.in/api/users/2")
    assert response_with_janet.json()['data']['first_name'] == 'Janet'