import pytest


class TestPasswd:
    @pytest.mark.complete("passwd ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("passwd -")
    def test_2(self, completion):
        assert completion
