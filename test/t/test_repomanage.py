import pytest


class TestRepomanage:
    @pytest.mark.complete("repomanage ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("repomanage -")
    def test_2(self, completion):
        assert completion
