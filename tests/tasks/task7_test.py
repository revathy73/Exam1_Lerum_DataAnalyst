import pytest

from src.tasks.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        TestCase(given=[5, 16, 9, 14, 13, 20, 25], expected="Tuesday"),
        TestCase(given=[100, 1, 1, 1, 1, 999, 999], expected="Monday"),
        TestCase(given=[1, 300, 1, 1, 1, 999, 999], expected="Tuesday"),
        TestCase(given=[1, 1, 400, 1, 1, 999, 999], expected="Wednesday"),
        TestCase(given=[1, 1, 1, 410, 1, 999, 999], expected="Thursday"),
        TestCase(given=[1, 1, 1, 1, 310, 999, 999], expected="Friday"),
        TestCase(given=[2, 3, 4, 5, 6, 1000, 2000], expected="Friday"),
        TestCase(given=[7, 6, 5, 4, 3, 2, 1], expected="Monday"),
        TestCase(given=[0, 0, 1, 0, 0, 100, 100], expected="Wednesday"),
        TestCase(given=[0, 0, 0, 0, 1, 0, 0], expected="Friday"),
        TestCase(given=[-5, -4, -3, -2, -1, 999, 999], expected="Friday"),
        TestCase(given=[0, -1, -2, -3, -4, 5, 6], expected="Monday"),
        TestCase(given=[2147483647, 1, 1, 1, 1, 0, 0], expected="Monday"),
        TestCase(
            given=[
                -2147483648,
                -2147483647,
                -2147483646,
                -2147483645,
                -2147483644,
                0,
                0,
            ],
            expected="Friday",
        ),
        TestCase(given=[9, 4, 11, 10, 3, 20, 15], expected="Wednesday"),
        TestCase(given=[12, 15, 9, 16, 14, 30, 28], expected="Thursday"),
        TestCase(given=[20, 5, 18, 18, 17, 100, 101], expected="Monday"),
        TestCase(given=[5, 5, 5, 6, 5, 100, 100], expected="Thursday"),
        TestCase(given=[5, 6, 5, 6, 7, 0, 0], expected="Friday"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> deliveries = {test_case.given}",
            expected=test_case.expected,
            actual=task7(deliveries=test_case.given),
        )
