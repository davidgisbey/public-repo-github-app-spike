from private_repo_github_app_spike import Prompt


class Greeter:
    def prompt(self) -> str:
        return f"Hello, this is the {Prompt().system_prompt()}! Really, it is."
