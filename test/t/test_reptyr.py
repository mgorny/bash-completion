import pytest


class TestReptyr:
    @pytest.mark.complete("reptyr ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("reptyr -")
    def test_2(self, completion):
        assert completion
