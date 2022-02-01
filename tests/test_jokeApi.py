import pytest
from src.clients import JokeApi


def test_get_random_joke_mocked_fixture_single(requests_mock, get_random_joke_mock):
    # Arrange
    requests_mock.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit",
        status_code=200,
        json={"type": "single", "joke": "Testing 1 joke"},
    )
    # Act
    joke = JokeApi.get_random_joke()
    # Assert
    assert joke == get_random_joke_mock


@pytest.mark.twopart
def test_get_random_joke_mocked_fixture_twopart(
    requests_mock,
    get_random_joke_mock,
):
    # Arrange
    requests_mock.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit",
        status_code=200,
        json={
            "type": "twopart",
            "setup": "Testing Setup",
            "delivery": "Testing delivery",
        },
    )
    # Act
    joke = JokeApi.get_random_joke()
    # Assert
    assert joke == get_random_joke_mock


def test_five_jokes_returns_five_jokes(get_random_joke_mock):
    # Arrange
    joke_count = []
    # Act
    joke_count += JokeApi.five_jokes()

    # Assert
    assert len(joke_count) == 5


def test_multiple_jokes_valid_input(get_random_joke_mock):
    # Arrange
    user_input = 3
    joke_count = []

    # Arrange
    joke_count += JokeApi.multiple_jokes(user_input)

    # Assert
    assert len(joke_count) == 3
