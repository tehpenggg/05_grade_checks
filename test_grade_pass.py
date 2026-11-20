import pytest
from grade_pass import has_passed


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, False),     
        (49, False),   
        (50, True),     
        (51, True),     
        (100, True),    
    ],
)
def test_grade_pass_valid_inputs(score, expected):
    result = has_passed(score)
    assert result is expected
    assert isinstance(result, bool)


@pytest.mark.parametrize(
    "score",
    [
        -1, 
        101, 
    ],
)
def test_grade_pass_out_of_range_raises_value_error(score):
    with pytest.raises(ValueError):
        has_passed(score)


@pytest.mark.parametrize(
    "score",
    [
        50.0,   
        "50",   
        True,  
        False,  
        None,   
    ],
)
def test_has_passed_invalid_type_raises_type_error(score):
    with pytest.raises(TypeError):
        has_passed(score)