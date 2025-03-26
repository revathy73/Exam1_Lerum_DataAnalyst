import pytest

from src.tasks.task9 import task9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        TestCase(given="9alexA", expected=False),
        TestCase(given="Ab1_", expected=False),
        TestCase(given="Abcdef1_ghiJK", expected=False),
        TestCase(given="alex_9", expected=False),
        TestCase(given="ALEX_9", expected=False),
        TestCase(given="AlexxA", expected=False),
        TestCase(given="_Alex9", expected=False),
        TestCase(given="Alex_9_", expected=False),
        TestCase(given="Alex-9", expected=False),
        TestCase(given="Alex.9", expected=False),
        TestCase(given="Alex 9", expected=False),
        TestCase(given="Alex+9", expected=False),
        TestCase(given="aB3__", expected=False),
        TestCase(given="Abc_def", expected=False),
        TestCase(given="a1234", expected=False),
        TestCase(given="A1234", expected=False),
        TestCase(given="Aa1_____", expected=False),
        TestCase(given="Alex_9", expected=True),
        TestCase(given="Aa___9", expected=True),
        TestCase(given="Zy9_xx", expected=True),
        TestCase(given="z9___X", expected=True),
        TestCase(given="A1b_c", expected=True),
        TestCase(given="Abcdef1_ghiJ", expected=True),
        TestCase(given="Abc12", expected=True),
        TestCase(given="A0000b", expected=True),
        TestCase(given="Abcdefghij9", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> username = {test_case.given}",
            expected=test_case.expected,
            actual=task9(username=test_case.given),
        )
