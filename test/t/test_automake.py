import pytest


class TestAutomake:
    @pytest.mark.complete("automake ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("automake -")
    def test_2(self, completion):
        assert completion
