import pytest

from src.tasks.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        TestCase(given="A", expected="Alice"),
        TestCase(given="B", expected="Bob"),
        TestCase(given="C", expected="Carol"),
        TestCase(given="D", expected="David"),
        TestCase(given="AAC", expected="Alice"),
        TestCase(given="BBD", expected="Bob"),
        TestCase(given="CCAB", expected="Carol"),
        TestCase(given="ABABA", expected="Alice"),
        TestCase(given="CBBDAAB", expected="Bob"),
        TestCase(given="CCACCCB", expected="Carol"),
        TestCase(given="DDDABC", expected="David"),
        TestCase(given="ABCCCD", expected="Carol"),
        TestCase(given="DAAAD", expected="Alice"),
        TestCase(given="DCBDDD", expected="David"),
        TestCase(given="BACADAB", expected="Alice"),
        TestCase(given="BDDBB", expected="Bob"),
        TestCase(given="CCDCC", expected="Carol"),
        TestCase(given="ADDDDA", expected="David"),
        TestCase(given="ABCDABCDABBB", expected="Bob"),
        TestCase(given="AAAAABBCD", expected="Alice"),
        TestCase(given="CCCCABAB", expected="Carol"),
        TestCase(given="DDDABCDA", expected="David"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> votes = {test_case.given}",
            expected=test_case.expected,
            actual=task2(votes=test_case.given),
        )
