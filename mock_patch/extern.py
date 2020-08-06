from unittest.mock import patch

from func.foo import foo_func


@patch("func.foo.bar_func", lambda *args: "This is from mock")
# @patch("func.bar.bar_func", lambda *args: "This is from mock")
def test_foo():
    foo = foo_func()
    print(foo)
    assert foo == "This is from mock"
