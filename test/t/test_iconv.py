import pytest


class TestIconv:
    @pytest.mark.complete("iconv -", xfail="! iconv --help &>/dev/null")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("iconv -f UTF")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("iconv ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("iconv -f ")
    def test_4(self, completion):
        assert "..." not in completion
