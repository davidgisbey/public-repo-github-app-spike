from basic_app import Greeter


def test_greet_returns_expected_message() -> None:
    assert Greeter().greet("World") == "Hello, World!"
