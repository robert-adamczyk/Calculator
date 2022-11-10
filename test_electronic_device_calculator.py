from unittest.mock import Mock, patch

import pytest

from calculator import Calculator, NoBatteryError


@pytest.fixture()
def calc():
    return Calculator()


def test_check_calculator_init(calc):
    assert calc.battery == 100


def test_check_battery_should_raise_no_battery_error(calc):
    calc.battery = 0
    with pytest.raises(NoBatteryError):
        calc.check_battery()


@pytest.mark.parametrize("given_a,given_b,expected_value", [(1, 2, 3), (-10, 5, -5), (100, -100, 0)])
def test_check_add(calc, given_a, given_b, expected_value):
    # Given
    # When
    result = calc.add(given_a, given_b)
    # Then
    assert result == expected_value


@pytest.mark.parametrize("given_a,given_b,expected_value", [(10, 20, -10), (-100, -200, 100), (100, 98, 2)])
def test_check_subtract(calc, given_a, given_b, expected_value):
    # Given
    # When
    result = calc.subtract(given_a, given_b)
    # Then
    assert result == expected_value


@pytest.mark.parametrize("given_a,given_b,expected_value", [(10, 20, 200), (-2, -6, 12), (250, 0, 0), (10, -5, -50)])
def test_check_multiply(calc, given_a, given_b, expected_value):
    # Given
    # When
    result = calc.multiply(given_a, given_b)
    # Then
    assert result == expected_value


def test_divide_should_raise_value_error(calc):
    with pytest.raises(ValueError):
        calc.divide(100, 0)


@pytest.mark.parametrize("given_a,given_b,expected_value",
                         [(20, 10, 2), (-3, 2, -1.50), (-200, -100, 2), (0, -5, -0.0)])
def test_check_divide(calc, given_a, given_b, expected_value):
    assert calc.divide(given_a, given_b) == expected_value


@pytest.mark.parametrize("given_a,expected_value", [(2, 4), (-3, 9), (0, 0)])
def test_check_square(calc, given_a, expected_value):
    assert calc.square(given_a) == expected_value


@pytest.mark.parametrize("given_a,given_power,expected_value",
                         [(2, 2, 4), (2, 4, 16), (3, 4, 81), (1, 10, 1)])
def test_check_n_to_power_of(calc, given_a, given_power, expected_value):
    assert calc.n_to_power_of(given_a, given_power,) == expected_value


@pytest.mark.parametrize("given_a,expected_value", [(2, True), (1, False), (100, True), (-33, False), (-504, True)])
def test_check_is_even(calc, given_a, expected_value):
    assert calc.is_even(given_a) is expected_value


@pytest.mark.parametrize("given_values,expected_result", [([10, 20, -20], 10), ([-5, 7, -2, -10, 50], 40)])
def test_check_add_multiple_values(calc, given_values, expected_result):
    # Given
    # When
    # Then
    assert calc.add(*given_values) == expected_result


def test_battery_by_calculate_100x_times(calc):
    for iteration in range(0, 102):
        value = 2
        try:
            calc.add(value, value)
        except NoBatteryError:
            assert True


def test_charge_battery(calc):
    # Given
    calc.battery = 10
    # When
    calc.charge_battery(20)
    # Then
    assert calc.battery == 30


def test_overcharging_the_battery_battery(calc):
    # Given
    calc.battery = 10
    # When
    calc.charge_battery(120)
    # Then
    assert calc.battery == 100


@pytest.mark.parametrize("given_data,expected_result",
                         [([["1", "2", "3", "4", "5"], ["2", "4", "1", "12"]], [3.0, 4.75]),
                          ([["1", "2"], ["2", "2", "2"], ["1", "1", "1", "5", "2"]], [1.5, 2.0, 2.0])])
def test_check_avg_file(given_data, expected_result):
    mock = Mock(return_value=given_data)

    with patch("calculator.Calculator._get_content", mock):
        calc = Calculator(filename="fake.txt")
        assert calc.avg_file() == expected_result


@pytest.mark.parametrize("given_data,expected_result",
                         [([["1", "3"], ["2", "4", "12"]], [[1.0, 3.0], [2.0, 4.0, 12.0]])])
def test_check_ensure_casted_data(given_data, expected_result):
    mock = Mock(return_value=given_data)

    with patch("calculator.Calculator._get_content", mock):
        calc = Calculator(filename="fake.txt")
        assert calc._ensure_casted_data() == expected_result


@pytest.mark.parametrize("given_data,expected_result",
                         [([["1", "3"], ["2", "4", "12"]], [["1", "3"], ["2", "4", "12"]])])
def test_check_get_content(given_data, expected_result):
    mock = Mock(return_value=given_data)

    with patch("calculator.Calculator._get_content", mock):
        calc = Calculator(filename="fake.txt")
        assert calc._get_content() == expected_result


def test_get_content2():
    calc = Calculator(filename="numbers.txt")
    result = calc._get_content()
    expected_result = [['1', '3\n'], ['2', '5.5', '3\n'], ['3', '1', '7', '5', '2']]
    assert result == expected_result
