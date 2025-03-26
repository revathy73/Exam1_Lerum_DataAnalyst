import pytest

from src.tasks.task1 import task1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask1:
    test_cases = [
        TestCase(given="S", expected="Sunny"),
        TestCase(given="C", expected="Cloudy"),
        TestCase(given="R", expected="Rainy"),
        TestCase(given="T", expected="Storm"),
        TestCase(given="SRS", expected="Rainy"),
        TestCase(given="CTC", expected="Storm"),
        TestCase(given="RCR", expected="Cloudy"),
        TestCase(given="TST", expected="Sunny"),
        TestCase(given="SCRTS", expected="Rainy"),
        TestCase(given="SSSSS", expected="Sunny"),
        TestCase(given="TTCTT", expected="Cloudy"),
        TestCase(given="RSTRS", expected="Storm"),
        TestCase(given="SCRTCSR", expected="Storm"),
        TestCase(given="CRSSSRC", expected="Sunny"),
        TestCase(given="CCCCRCCCC", expected="Rainy"),
        TestCase(given="SSSSCSSSS", expected="Cloudy"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> weather = {test_case.given}",
            expected=test_case.expected,
            actual=task1(weather=test_case.given),
        )
