import pytest


class TestUsermod:
    @pytest.mark.complete("usermod ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("usermod -")
    def test_2(self, completion):
        assert completion
