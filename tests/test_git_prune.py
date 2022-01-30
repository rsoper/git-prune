from git_prune import __version__
from git_prune import main
import unittest


class GitPruneTests(unittest.TestCase):

    def setUp(self):
        self.gitprune = main.GitPrune()

    def test_version(self):
        assert __version__ == '0.0.9'

    def test_shell_CMD(self):
        shell_CMD = self.gitprune.shell_CMD('echo testing123')
        assert shell_CMD == 'testing123'
        assert type(shell_CMD) == str

    def test_get_remote_branches(self):
        remote_branches = self.gitprune.get_remote_branches()
        assert 'master' in remote_branches
        assert type(remote_branches) == list
        assert remote_branches != []

    def test_get_local_branches(self):
        local_branches = self.gitprune.get_local_branches()
        assert 'master' in local_branches
        assert type(local_branches) == list
        assert local_branches != []

    def test_not_remote(self):
        assert type(self.gitprune.not_remote) == list
        assert self.gitprune.not_remote == []

    def test_delete_branches(self):
        self.gitprune.shell_CMD('git branch -c master new-branch')
        assert 'new-branch' in self.gitprune.get_local_branches()
        self.gitprune.shell_CMD('git checkout new-branch')
        self.gitprune.not_remote.append('new-branch')
        assert 'new-branch' in self.gitprune.not_remote
        self.gitprune.delete_branches()
        assert 'new-branch' not in self.gitprune.get_local_branches()

    # def test_end_to_end(self):
