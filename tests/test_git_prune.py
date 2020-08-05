from git_prune import __version__
from git_prune import main
import unittest


class GitPruneTests(unittest.TestCase):

    def setUp(self):
        self.gitprune = main.git_prune()

    def test_version(self):
        assert __version__ == '0.0.7'

    def test_shellCMD(self):
        shellCMD = self.gitprune.shellCMD('echo testing123')
        assert shellCMD == 'testing123'
        assert type(shellCMD) == str

    def test_get_remote_branches(self):
        remoteBranches = self.gitprune.get_remote_branches()
        assert 'master' in remoteBranches
        assert type(remoteBranches) == list
        assert remoteBranches != []

    def test_get_local_branches(self):
        localBranches = self.gitprune.get_local_branches()
        assert 'master' in localBranches
        assert type(localBranches) == list
        assert localBranches != []

    def test_not_remote(self):
        assert type(self.gitprune.notRemote) == list
        assert self.gitprune.notRemote == []

    def test_delete_branches(self):
        self.gitprune.shellCMD('git branch -c master new-branch')
        assert 'new-branch' in self.gitprune.get_local_branches()
        self.gitprune.shellCMD('git checkout new-branch')
        self.gitprune.notRemote.append('new-branch')
        assert 'new-branch' in self.gitprune.notRemote
        self.gitprune.delete_branches()
        assert 'new-branch' not in self.gitprune.get_local_branches()
