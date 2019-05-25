import pytest


class TestXmodmap:
    @pytest.mark.complete("xmodmap ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xmodmap -")
    def test_2(self, completion):
        assert completion
