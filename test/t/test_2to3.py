import pytest


class Test2to3:
    @pytest.mark.complete("2to3 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("2to3 -")
    def test_2(self, completion):
        assert completion
