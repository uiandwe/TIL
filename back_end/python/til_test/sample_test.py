"""Sample test code."""


def hello(name):
    """Return greeting message."""
    return 'Hello, {}!'.format(name)


def test_hello():
    """hello function test."""
    assert hello('JOKER') == 'Hello, JOKER!'
