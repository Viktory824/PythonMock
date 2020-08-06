from unittest.mock import patch


def bar():
    return "Iam bar"


def foo():
    try:
        return bar()
    except TypeError:
        print("\n\nTypeError occurs\n\n")
        # print("\n\nAttributeError\n\n")


def test_errors():
    with patch('test_errors.bar', side_effect=TypeError):
        assert foo() is None
