from unittest.mock import patch


def foo():
    return input()


@patch('builtins.input', lambda *args: 'privet')
def test_example_func():
    assert foo() == 'privet'
