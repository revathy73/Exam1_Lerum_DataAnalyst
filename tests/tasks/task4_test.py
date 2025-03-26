import pytest

from src.tasks.task4 import task4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask4:
    test_cases = [
        TestCase(given="10km", expected="6mi"),
        TestCase(given="1km", expected="1mi"),
        TestCase(given="3km", expected="2mi"),
        TestCase(given="4KM", expected="2mi"),
        TestCase(given="5kM", expected="3mi"),
        TestCase(given="16Km", expected="10mi"),
        TestCase(given="160km", expected="99mi"),
        TestCase(given="161km", expected="100mi"),
        TestCase(given="200km", expected="124mi"),
        TestCase(given="201KM", expected="125mi"),
        TestCase(given="999km", expected="620mi"),
        TestCase(given="0km", expected="0mi"),
        TestCase(given="62MI", expected="100km"),
        TestCase(given="1mi", expected="2km"),
        TestCase(given="2MI", expected="3km"),
        TestCase(given="3Mi", expected="5km"),
        TestCase(given="4mI", expected="6km"),
        TestCase(given="5mi", expected="8km"),
        TestCase(given="500mi", expected="804km"),
        TestCase(given="123MI", expected="198km"),
        TestCase(given="321mi", expected="516km"),
        TestCase(given="999mi", expected="1607km"),
        TestCase(given="10Mi", expected="16km"),
        TestCase(given="11mI", expected="18km"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> distance = {test_case.given}",
            expected=test_case.expected,
            actual=task4(distance=test_case.given),
        )
