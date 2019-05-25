import pytest


@pytest.mark.bashcomp(pre_cmds=("export RI='-d ri'",))
class TestRi:
    @pytest.mark.complete("ri -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ri --dump=ri/")
    def test_2(self, completion):
        assert completion == "BashCompletion/ cache.ri".split()

    @pytest.mark.complete("ri BashCompletio")
    def test_3(self, completion):
        assert completion == "BashCompletion"
