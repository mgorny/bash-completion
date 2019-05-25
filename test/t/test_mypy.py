import pytest


class TestMypy:
    @pytest.mark.complete("mypy ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mypy --")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("mypy --non-existent-option=--")
    def test_3(self, completion):
        assert not completion
