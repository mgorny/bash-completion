import pytest


class TestPwck:
    @pytest.mark.complete("pwck ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pwck -")
    def test_2(self, completion):
        assert completion
