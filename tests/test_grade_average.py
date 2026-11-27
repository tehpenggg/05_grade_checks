import pytest
from grade_average import calculate_average

@pytest.mark.parametrize(
    "mark_one, mark_two, expected_mark",
[
    (0,0,0.0),
    (100,100,100.0),
    (60,80,70.0),
    (50,51,50.5),
    (0,100,50.0,)
],
)

def test_calculate_average_valid_inputs(mark_one, mark_two, expected_mark):
    result = calculate_average(mark_one, mark_two)
    assert result == expected_mark 


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),    
        (50, -1),    
        (101, 50),   
        (50, 101),   
    ],
)
def test_calculate_average_out_of_range_raises_error(mark_one, mark_two):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (50.5, 60),   
        ("50", 60),    
        (True, 50),    
        (False, 50),  
        (None, 50),    
        (50, [60]),   
    ],
)
def test_calculate_average_invalid_type_raises_type_error(mark_one, mark_two):
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)