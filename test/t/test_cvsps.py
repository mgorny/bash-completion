import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/cvs",))
class TestCvsps:
    @pytest.mark.complete("cvsps -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cvsps ")
    def test_2(self, completion):
        assert [x for x in completion if ":pserver:" in x]
