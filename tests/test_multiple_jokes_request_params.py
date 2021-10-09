import pytest

from src.schemas import MultipleJokesRequestParams


@pytest.fixture
def multipleJokesRequestParams(**kwargs):
    return multipleJokesRequestParams(**kwargs)
    

def test_is_in_range_with_valid_range():
    # Arrange
    valid_count = 5
    
    # Act
    MultipleJokesRequestParams(
        count=valid_count,
        language="pl"
    )
    
    # Assert
    pass # does not raise ValueError


def test_is_in_range_with_invalid_range():
    
    with pytest.raises(Exception) as excinfo:
        
        # Arrange
        not_valid_count = 25

        # Act
        MultipleJokesRequestParams(
            count=not_valid_count,
            language="pl"
        )
    
    # Assert
    assert "Out of range! Try 1 to 10." in str(excinfo.value)
    
    
def test_is_in_lang_list():
    
    # Arrange
    valid_language = "lt"

    # Act
    MultipleJokesRequestParams(
            count=1,
            language=valid_language
        )
    # Assert
    pass # does not raise ValueError


def test_not_in_lang_list():
    
    with pytest.raises(Exception) as excinfo:
        
        # Arrange
        not_valid_language = "cz"
        
        # Act
        MultipleJokesRequestParams(
            count=1,
            language=not_valid_language
        )
    # Assert
    assert "Wrong input!" in str(excinfo)