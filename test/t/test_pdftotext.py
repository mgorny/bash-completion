import pytest


class TestPdftotext:
    @pytest.mark.complete("pdftotext ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pdftotext -")
    def test_2(self, completion):
        assert completion
