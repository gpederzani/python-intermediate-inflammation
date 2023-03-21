"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


import pytest
...
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[-2, 0, 6], [9, 1, 17], [-5, -3, 0]], [-5, -3, 0]),
    ])
def test_daily_min(test, expected):
    """Test that min function works for array of zeros
     and of mixed-sign integers.
     """
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[-2, 0, 6], [9, 1, 17], [-5, -3, 0]], [9, 1, 17]),
    ])
def test_daily_max(test, expected):
    """Test that min function works for array of zeros
    and of mixed-sign integers.
    """
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))
