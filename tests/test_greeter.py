from basic_app import Greeter
from private_repo_github_app_spike import Prompt


def test_greet_returns_private_repo_system_prompt() -> None:
    assert Greeter().prompt() == f"Hello, this is the {Prompt().system_prompt()}! Really, it is."
