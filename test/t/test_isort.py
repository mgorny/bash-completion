import pytest


class TestIsort:
    @pytest.mark.complete("isort ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("isort -")
    def test_2(self, completion):
        assert completion
