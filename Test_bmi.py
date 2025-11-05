from Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    result = calculate_bmi(45, 1.63)
    assert result == -1

def test_bmi_normal_weight():
    result = calculate_bmi(58, 1.62)
    assert result == 0

def test_bmi_over_weight():
    result = calculate_bmi(75, 1.64)
    assert result == 1
