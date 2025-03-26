import pytest

from src.tasks.task6 import task6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask6:
    test_cases = [
        TestCase(
            given=[
                "anna|se|ELEC-4932",
                "bo|no|HOME-118",
                "carl|SE|SPORT-77",
                "dina|dk|ELEC-200",
                "erik|se|HOME-555",
                "fred|se|ELEC-4932",
            ],
            expected=["ELEC", "SPORT", "HOME"],
        ),
        TestCase(
            given=[
                "Sebastian|No|ELEC-4932",
                "selena|Dk|HOME-118",
                "SEth|dk|SPORT-77",
                "dina|dk|ELEC-200",
                "erik|se|HOME-555",
            ],
            expected=["HOME"],
        ),
        TestCase(given=[], expected=[]),
        TestCase(
            given=["mary|dk|HOME-1", "john|NO|ELEC-2", "li|fi|SPORT-3"], expected=[]
        ),
        TestCase(given=["anna|se|ELEC-1"], expected=["ELEC"]),
        TestCase(
            given=["a|SE|HOME-1", "b|se|HOME-2", "c|Se|HOME-3"], expected=["HOME"]
        ),
        TestCase(
            given=["a|se|SPORT-1", "b|no|ELEC-5", "c|se|ELEC-7", "d|se|SPORT-9"],
            expected=["SPORT", "ELEC"],
        ),
        TestCase(
            given=[
                "x|se|ELEC-1",
                "y|se|HOME-1",
                "z|se|SPORT-1",
                "w|se|ELEC-2",
                "v|se|HOME-2",
            ],
            expected=["ELEC", "HOME", "SPORT"],
        ),
        TestCase(
            given=["m|fi|ELEC-1", "n|dk|HOME-1", "o|se|SPORT-1"], expected=["SPORT"]
        ),
        TestCase(
            given=["p|sE|CODE-ABC123", "q|SE|TOOLS-99", "r|no|CODE-XYZ"],
            expected=["CODE", "TOOLS"],
        ),
        TestCase(
            given=["a|se|ELEC-1", "a|se|ELEC-1", "b|se|ELEC-1"], expected=["ELEC"]
        ),
        TestCase(
            given=[
                "a|se|GARDEN-1",
                "b|se|BOOKS-2",
                "c|se|TOYS-3",
                "d|no|GARDEN-9",
                "e|se|GARDEN-4",
                "f|se|BOOKS-5",
            ],
            expected=["GARDEN", "BOOKS", "TOYS"],
        ),
        TestCase(
            given=[
                "a|se|HOME-10",
                "b|no|ELEC-20",
                "c|se|ELEC-30",
                "d|dk|SPORT-40",
                "e|se|BOOKS-50",
                "f|se|HOME-60",
            ],
            expected=["HOME", "ELEC", "BOOKS"],
        ),
        TestCase(
            given=[
                "g|fi|ELEC-1",
                "h|is|SPORT-2",
                "i|Se|HOME-3",
                "j|NO|HOME-4",
                "k|se|ELEC-5",
                "l|DK|SPORT-6",
                "m|SE|GAMES-7",
            ],
            expected=["HOME", "ELEC", "GAMES"],
        ),
        TestCase(
            given=[
                "u|se|A-1",
                "v|se|B-2",
                "w|no|C-3",
                "x|se|A-4",
                "y|se|C-5",
                "z|se|B-6",
                "aa|se|D-7",
                "ab|fi|E-8",
                "ac|SE|C-9",
                "ad|dk|A-10",
            ],
            expected=["A", "B", "C", "D"],
        ),
        TestCase(
            given=["r|no|ELEC-1", "s|se|SPORT-2", "t|se|HOME-3", "u|se|ELEC-4"],
            expected=["SPORT", "HOME", "ELEC"],
        ),
        TestCase(
            given=[
                "a|se|Z-100",
                "b|se|Z-101",
                "c|se|Y-200",
                "d|se|X-300",
                "e|se|Y-201",
                "f|se|X-301",
            ],
            expected=["Z", "Y", "X"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> orders = {test_case.given}",
            expected=test_case.expected,
            actual=task6(orders=test_case.given),
        )
