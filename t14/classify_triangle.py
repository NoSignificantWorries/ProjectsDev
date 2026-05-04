from typing import Optional


def classify_triangle(a: float, b: float, c: float) -> Optional[str]:
    if a <= 0 or b <= 0 or c <= 0:
        return None

    if a + b <= c or b + c <= a or a + c <= b:
        return None

    if a == b and a == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "usual"

