import pytest


class TestPngfix:
    @pytest.mark.complete("pngfix ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pngfix -")
    def test_2(self, completion):
        assert completion
