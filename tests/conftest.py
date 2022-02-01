import pytest
from src.clients import JokeApi


@pytest.fixture
def get_random_joke_mock(requests_mock, request):
    marker = request.node.get_closest_marker("twopart")
    params = {
        "url": "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit",
        "status_code": 200,
        "json": {"type": "single", "joke": "Testing 1 joke"},
    }
    if marker is None:
        requests_mock.get(**params)
    else:
        params["json"] = {
            "type": "twopart",
            "setup": "Testing Setup",
            "delivery": "Testing delivery",
        }
        requests_mock.get(**params)
    return JokeApi.get_random_joke()
