import pytest

from src.tasks.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        TestCase(given="", expected=""),
        TestCase(given="a", expected="A"),
        TestCase(given="A", expected="A"),
        TestCase(given="!", expected="!"),
        TestCase(given="ab", expected="Ba"),
        TestCase(given="Ab", expected="BA"),
        TestCase(given="aB", expected="Ba"),
        TestCase(given="Zz", expected="ZZ"),
        TestCase(given="abc", expected="CbA"),
        TestCase(given="abcd", expected="DcBa"),
        TestCase(given="Hello!", expected="!oLlEH"),
        TestCase(given="HELLO", expected="OLLEH"),
        TestCase(given="hElLo", expected="OLLEH"),
        TestCase(given="a1b2c3", expected="3c2b1a"),
        TestCase(given="a!b?c", expected="C?B!A"),
        TestCase(given="12345", expected="54321"),
        TestCase(given="AaAa", expected="AAAA"),
        TestCase(given="zzzz", expected="ZzZz"),
        TestCase(given="Zzz", expected="ZzZ"),
        TestCase(given=" ab", expected="Ba "),
        TestCase(given="mixed CASE 123", expected="321 ESAC dExIm"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> text = {test_case.given}",
            expected=test_case.expected,
            actual=task8(text=test_case.given),
        )
