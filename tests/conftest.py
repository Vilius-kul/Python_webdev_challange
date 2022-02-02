import pytest
from src.clients import JokeApi


@pytest.fixture
def mock_single_joke_response(requests_mock):
    return requests_mock.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit",
        status_code=200,
        json={"type": "single", "joke": "Testing 1 joke"},
    )


@pytest.fixture
def mock_twopart_joke_response(requests_mock):
    return requests_mock.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit",
        status_code=200,
        json={
            "type": "twopart",
            "setup": "Testing Setup",
            "delivery": "Testing delivery",
        },
    )
