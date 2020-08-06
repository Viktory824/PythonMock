from unittest.mock import patch


def foo():
    return input(), input(), input(), input()


def test_side_effect():
    with patch('builtins.input', side_effect=("one", "two", "three", "four")):
        assert foo() == ("one", "two", "three", "four")
        # assert input() == "four"
