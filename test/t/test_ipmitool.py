import pytest


class TestIpmitool:
    @pytest.mark.complete("ipmitool ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ipmitool -")
    def test_2(self, completion):
        assert completion
