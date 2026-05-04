import pytest

from classify_triangle import classify_triangle as basic_func
from classify_triangle_buggy import classify_triangle as buggy_func

ALL_IMPLEMENTATIONS = [
    ("basic_func", basic_func),
    ("buggy_func", buggy_func),
]


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_equilateral_all_sides_equal(name, func):
    assert func(3, 3, 3) == "equilateral"
    assert func(5.5, 5.5, 5.5) == "equilateral"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_isosceles_two_sides_equal_ab(name, func):
    assert func(5, 5, 3) == "isosceles"
    assert func(5, 5, 7) == "isosceles"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_isosceles_two_sides_equal_ac(name, func):
    assert func(5, 3, 5) == "isosceles"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_isosceles_two_sides_equal_bc(name, func):
    assert func(3, 5, 5) == "isosceles"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_usual_triangle_all_sides_different(name, func):
    assert func(3, 4, 5) == "usual"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_floating_point_triangle(name, func):
    assert func(3.5, 4.5, 5.5) == "usual"
    assert func(2.5, 2.5, 3.5) == "isosceles"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_near_equilateral_triangle(name, func):
    assert func(3, 3, 3.0001) == "isosceles"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_negative_side_returns_none(name, func):
    assert func(-1, 3, 4) is None
    assert func(3, -2, 4) is None
    assert func(3, 4, -5) is None


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_zero_side_returns_none(name, func):
    assert func(0, 3, 4) is None
    assert func(3, 0, 4) is None
    assert func(3, 4, 0) is None


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_all_negative_sides_returns_none(name, func):
    assert func(-1, -2, -3) is None


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_violates_triangle_inequality_sum_equal(name, func):
    assert func(3, 4, 7) is None
    assert func(5, 5, 10) is None


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_violates_triangle_inequality_sum_less(name, func):
    assert func(2, 3, 10) is None
    assert func(10, 2, 3) is None


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_extremely_small_positive_sides(name, func):
    assert func(1e-10, 1e-10, 1e-10) == "equilateral"


@pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
def test_large_values(name, func):
    assert func(1e10, 1e10, 1e10) == "equilateral"
