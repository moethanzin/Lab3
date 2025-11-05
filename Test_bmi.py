from Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    result = calculate_bmi(1.73, 43)
    assert result == -1

def test_bmi_normal_weight():
    result = calculate_bmi(1.73,56)
    assert result == 0

def test_bmi_over_weight():
    result = calculate_bmi(1.73, 80)
    assert result == 1
