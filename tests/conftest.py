import pytest

from git_prune.main import GitPrune


@pytest.fixture(scope="function")
def gitprune():
    git_prune = GitPrune()
    git_prune.shell_cmd("git branch setup")
    yield git_prune
    if git_prune.not_remote:
        git_prune.delete_branches()
