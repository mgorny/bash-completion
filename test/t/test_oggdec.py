import pytest


class TestOggdec:
    @pytest.mark.complete("oggdec ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("oggdec --")
    def test_2(self, completion):
        assert completion
