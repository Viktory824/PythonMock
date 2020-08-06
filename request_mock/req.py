import pytest
import requests
import requests_mock


def foo():
    response = requests.get("http://google.com")
    print(response.status_code)
    return response


@pytest.fixture
def mock():
    with requests_mock.Mocker() as mock_instance:
        yield mock_instance


def test_foo():
    # https://requests-mock.readthedocs.io/en/latest/matching.html
    # mock.get("http://google.com", status_code=404)

    # resp = requests.get("http://ya.ru")
    # print(resp.status_code)
    response = foo()
    assert response.status_code == 404
