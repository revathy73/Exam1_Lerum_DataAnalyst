import pytest

from src.tasks.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask5:
    test_cases = [
        TestCase(given=[3, 5, 7, 2], expected=[8, 12, 9, 4]),
        TestCase(given=[], expected=[-1]),
        TestCase(given=[4], expected=[16]),
        TestCase(given=[0], expected=[0]),
        TestCase(given=[-3], expected=[9]),
        TestCase(given=[2, 9], expected=[11, 81]),
        TestCase(given=[5, -5], expected=[0, 25]),
        TestCase(given=[0, 0], expected=[0, 0]),
        TestCase(given=[0, 7, 0], expected=[7, 7, 0]),
        TestCase(given=[10, 0, -10], expected=[10, -10, 100]),
        TestCase(given=[6, -2, -3], expected=[4, -5, 9]),
        TestCase(given=[-1, -2, -3, -4], expected=[-3, -5, -7, 16]),
        TestCase(given=[1, -1, 1, -1, 1], expected=[0, 0, 0, 0, 1]),
        TestCase(given=[-10, 10, -10, 10], expected=[0, 0, 0, 100]),
        TestCase(given=[7, 7, 7, 7], expected=[14, 14, 14, 49]),
        TestCase(given=[9, 7, 5, 3, 1], expected=[16, 12, 8, 4, 1]),
        TestCase(
            given=[1_000_000, 2_000_000, 3_000_000, 10],
            expected=[3_000_000, 5_000_000, 3_000_010, 100],
        ),
        TestCase(given=[2, 2, -1], expected=[4, 1, 1]),
        TestCase(given=[2, 3, 0], expected=[5, 3, 0]),
        TestCase(given=[1, 2, 3, 4, 5, 6], expected=[3, 5, 7, 9, 11, 36]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> scores = {test_case.given}",
            expected=test_case.expected,
            actual=task5(scores=test_case.given),
        )
