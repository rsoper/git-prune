import pytest

from git_prune.main import GitPrune


@pytest.fixture(scope="session")
def gitprune():
    gitprune = GitPrune()
    gitprune.shell_cmd("git branch setup")
    gitprune.not_remote.append("setup")
    return gitprune
