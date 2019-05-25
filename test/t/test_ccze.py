import pytest


class TestCcze:
    @pytest.mark.complete("ccze ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ccze -? ")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("ccze -o ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("ccze --plugin=")
    def test_4(self, completion):
        assert completion
