import pytest
from src.clients import JokeApi


def test_get_random_joke_single(mock_single_joke_response):
    # Arrange

    # Act
    joke = JokeApi.get_random_joke()
    # Assert
    assert joke == "Testing 1 joke"


def test_get_random_joke_twopart(mock_twopart_joke_response):
    # Arrange

    # Act
    joke = JokeApi.get_random_joke()
    # Assert
    assert joke == "Testing Setup... Testing delivery"


def test_five_jokes_returns_five_jokes(mock_single_joke_response):
    # Arrange
    joke_count = []
    # Act
    joke_count += JokeApi.five_jokes()

    # Assert
    assert len(joke_count) == 5


def test_multiple_jokes_valid_input(mock_single_joke_response):
    # Arrange
    user_input = 3
    joke_count = []

    # Arrange
    joke_count += JokeApi.multiple_jokes(user_input)

    # Assert
    assert len(joke_count) == 3
