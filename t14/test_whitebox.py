import pytest

from classify_triangle import classify_triangle as basic_func
from classify_triangle_buggy import classify_triangle as buggy_func

ALL_IMPLEMENTATIONS = [
    ("basic_func", basic_func),
    ("buggy_func", buggy_func),
]


class TestWhiteBox:
    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_a_less_or_equal_zero(self, name, func):
        assert func(-5, 3, 4) is None

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_b_less_or_equal_zero(self, name, func):
        assert func(3, -5, 4) is None

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_c_less_or_equal_zero(self, name, func):
        assert func(3, 4, -5) is None

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_boundary_zero_b_and_c(self, name, func):
        if name == "basic_func":
            assert func(3, 0, 4) is None
            assert func(3, 4, 0) is None
        else:
            result = func(3, 0, 4)
            assert result is None, f"Expected None for b=0, got {result}"

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_a_plus_b_less_or_equal_c(self, name, func):
        assert func(3, 3, 7) is None

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_b_plus_c_less_or_equal_a(self, name, func):
        assert func(10, 3, 4) is None

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_a_plus_c_less_or_equal_b(self, name, func):
        assert func(2, 10, 5) is None

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_boundary_equality_triangle(self, name, func):
        result = func(3, 4, 7)
        if name == "basic_func":
            assert result is None
        else:
            assert result is None, (
                f"Expected None for degenerate triangle, got {result}"
            )

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_all_sides_equal_equilateral(self, name, func):
        result = func(5, 5, 5)
        assert result == "equilateral", f"Expected 'equilateral', got {result}"

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_isosceles_variants(self, name, func):
        assert func(5, 5, 3) == "isosceles"  # a == b
        assert func(5, 3, 5) == "isosceles"  # a == c
        assert func(3, 5, 5) == "isosceles"  # b == c

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_equilateral_not_isosceles(self, name, func):
        result = func(4, 4, 4)
        assert result == "equilateral", (
            f"Equilateral triangle misclassified as {result}"
        )

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_path_all_sides_different(self, name, func):
        assert func(3, 4, 6) == "usual"

    @pytest.mark.parametrize("name,func", ALL_IMPLEMENTATIONS)
    def test_condition_order(self, name, func):
        result = func(3, 3, 3)
        assert result == "equilateral", "Equilateral check should come before isosceles"
