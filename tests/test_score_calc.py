from feedback.score_calc import calculate_average

def test_calculate_average():
    assert calculate_average([90, 80, 70]) == 80
    assert calculate_average([]) == 0
