import pytest


class TestNewusers:
    @pytest.mark.complete("newusers ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("newusers -")
    def test_2(self, completion):
        assert completion
