import pytest
from src.schemas import MultipleJokesRequestParams


def test_is_in_range_with_valid_range():
    # Arrange
    valid_count = 5

    # Act
    result = MultipleJokesRequestParams(count=valid_count, language="pl")

    # Assert
    assert result.count == valid_count


def test_is_not_in_range_with_invalid_range():

    # Arrange
    not_valid_count = 25

    with pytest.raises(Exception) as excinfo:
        # Act
        MultipleJokesRequestParams(count=not_valid_count, language="pl")

    # Assert
    assert "Out of range! Try 1 to 10." in str(excinfo.value)


def test_is_in_lang_list():

    # Arrange
    valid_language = "lt"
    # Act
    result = MultipleJokesRequestParams(count=1, language=valid_language)
    # Assert
    assert result.language == valid_language


def test_not_in_lang_list():

    # Arrange
    not_valid_language = "cz"

    with pytest.raises(Exception) as excinfo:
        # Act
        MultipleJokesRequestParams(count=1, language=not_valid_language)
    # Assert
    assert (
        "Wrong input! Please type 'pl' for Polish,'lt' for Lithuanian, 'da' for Danish or 'ru' for Russian"
        in str(excinfo)
    )
