import pytest


class TestLuac:
    @pytest.mark.complete("luac ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("luac -")
    def test_2(self, completion):
        assert completion
