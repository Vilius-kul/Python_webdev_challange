from src.schemas import MultipleJokesRequestParams

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
    # Arrange
    valid_count = 25
    
    # Act
    MultipleJokesRequestParams(
        count=valid_count,
        language="pl"
    )
    
    # Assert
    pass # does not raise ValueError
