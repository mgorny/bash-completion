import pytest


class TestXzdec:
    @pytest.mark.complete("xzdec ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xzdec -")
    def test_2(self, completion):
        assert completion
