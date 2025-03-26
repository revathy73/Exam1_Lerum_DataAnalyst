import pytest

from src.tasks.task10 import task10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask10:
    test_cases = [
        TestCase2(
            given1=["Anna", "Bob", "anna", "Eve", "Anna"],
            given2="anna",
            expected=6,
        ),
        TestCase2(given1=["Alice", "Bob"], given2="Charlie", expected=0),
        TestCase2(given1=[], given2="any", expected=0),
        TestCase2(given1=["anna"], given2="Anna", expected=0),
        TestCase2(given1=["Ann"], given2="Anna", expected=0),
        TestCase2(given1=["x", "X", "x", "X"], given2="x", expected=6),
        TestCase2(
            given1=["Mike", "John", "mike", "JOHN", "MIKE"],
            given2="mike",
            expected=6,
        ),
        TestCase2(
            given1=["Ann", "Anna", "Anne", "annA", "An"],
            given2="Anna",
            expected=4,
        ),
        TestCase2(given1=["Eve", "Bob", "Carol", "ALICE"], given2="alice", expected=3),
        TestCase2(given1=["tom", "Jerry", "TOM"], given2="Tom", expected=2),
        TestCase2(
            given1=["Örjan", "anna", "ÖRJAN", "örjan"],
            given2="örjan",
            expected=5,
        ),
        TestCase2(
            given1=["a", "b", "a", "c", "a", "d", "a"],
            given2="A",
            expected=12,
        ),
        TestCase2(
            given1=["sam", "SAM", "SaM", "sAm", "max"],
            given2="sam",
            expected=6,
        ),
        TestCase2(
            given1=["Jean-Luc", "jean-luc", "Jean"],
            given2="JEAN-LUC",
            expected=1,
        ),
        TestCase2(given1=["José", "josé", "JOsé"], given2="JOSÉ", expected=3),
        TestCase2(
            given1=["x", "A", "x", "x", "a", "x", "x", "A", "x", "a"],
            given2="a",
            expected=21,
        ),
        TestCase2(given1=["Liam", "Noah", "Olivia", "Emma"], given2="Ava", expected=0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given1
        student = test_case.given2

        assert_equals(
            message=f"> classroom = {classroom}\n> student = {student}",
            expected=test_case.expected,
            actual=task10(classroom=classroom, student=student),
        )
