import pytest

from src.tasks.task3 import task3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        TestCase(
            given=[-2, 0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1], expected="January"
        ),
        TestCase(given=[-5, 0, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected="January"),
        TestCase(given=[5, -6, 0, 1, -2, 3, -4, 5, 6, 7, 8, 9], expected="February"),
        TestCase(given=[4, 3, -7, -2, 5, -6, 7, 8, 9, 10, 11, 12], expected="March"),
        TestCase(given=[10, 9, 8, -8, 7, 6, 5, -4, -3, 2, 1, 0], expected="April"),
        TestCase(given=[-3, -4, -5, 6, -9, 8, 9, 10, 11, 12, 13, 14], expected="May"),
        TestCase(given=[1, 2, -3, -4, -5, -10, 6, 7, 8, 9, 10, 11], expected="June"),
        TestCase(given=[10, 9, 8, 7, 6, 5, -11, 4, 3, 2, 1, 0], expected="July"),
        TestCase(
            given=[30, 25, 26, 28, 32, 38, 37, 12, 33, 31, 29, 21], expected="August"
        ),
        TestCase(
            given=[50, 60, 55, 70, 65, 80, 90, 85, 11, 100, 95, 120],
            expected="September",
        ),
        TestCase(
            given=[60, 62, 63, 64, 65, 66, 67, 68, 69, 18, 70, 71], expected="October"
        ),
        TestCase(
            given=[99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 21, 100], expected="November"
        ),
        TestCase(
            given=[200, 180, 175, 160, 150, 140, 130, 120, 110, 108, 107, 33],
            expected="December",
        ),
        TestCase(given=[13, 13, 14, -1, 0, 3, 2, 9, 7, 6, 8, 12], expected="April"),
        TestCase(
            given=[11, 21, 5, 53, 44, 55, 76, 75, 82, 91, 19, 11], expected="March"
        ),
        TestCase(
            given=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -100000000, 10], expected="November"
        ),
        TestCase(
            given=[-5, -4, -3, -2, -1, -6, -7, -8, -9, -12, -11, -20],
            expected="December",
        ),
        TestCase(
            given=[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12],
            expected="December",
        ),
        TestCase(
            given=[-20, -5, -4, -3, -2, -6, -7, -8, -9, -10, -11, -12],
            expected="January",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> temperatures = {test_case.given}",
            expected=test_case.expected,
            actual=task3(temperatures=test_case.given),
        )
