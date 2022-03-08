from git_prune import __version__
from git_prune.main import GitPrune


def setup_module(module):
    global gitprune
    print("*****SETUP*****")
    gitprune = GitPrune()
    gitprune.shell_cmd("git branch setup")
    gitprune.not_remote.append("setup")


def teardown_module(module):
    print("*****TEARDOWN*****")


def test_version():
    assert __version__ == "0.0.10"


def test_shell_CMD():
    shell_CMD = gitprune.shell_cmd("echo testing123")
    assert shell_CMD == "testing123"
    assert type(shell_CMD) == str


def test_get_remote_branches():
    remote_branches = gitprune.get_remote_branches()
    assert "master" in remote_branches
    assert type(remote_branches) == list
    assert remote_branches != []


def test_get_local_branches():
    local_branches = gitprune.get_local_branches()
    assert "master" in local_branches
    assert type(local_branches) == list
    assert local_branches != []


def test_not_remote():
    assert type(gitprune.not_remote) == list
    assert gitprune.not_remote == ["setup"]


def test_delete_branches():
    print(gitprune.shell_cmd("git branch new-branch"))
    assert "new-branch" in gitprune.get_local_branches()
    gitprune.shell_cmd("git checkout new-branch")
    gitprune.not_remote.append("new-branch")
    assert "new-branch" in gitprune.not_remote
    gitprune.delete_branches()
    assert "new-branch" not in gitprune.get_local_branches()
