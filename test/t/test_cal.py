import pytest


class TestCal:
    @pytest.mark.complete("cal ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cal -")
    def test_2(self, completion):
        assert completion
