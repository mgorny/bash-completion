import pytest


class TestNcftp:
    @pytest.mark.complete("ncftp ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ncftp -")
    def test_2(self, completion):
        assert completion
