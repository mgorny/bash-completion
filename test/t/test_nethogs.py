import pytest


class TestNethogs:
    @pytest.mark.complete("nethogs ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("nethogs -")
    def test_2(self, completion):
        assert completion
