import pytest


class TestAutoscan:
    @pytest.mark.complete("autoscan ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("autoscan -")
    def test_2(self, completion):
        assert completion
