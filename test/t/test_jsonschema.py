import pytest


class TestJsonschema:
    @pytest.mark.complete("jsonschema ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("jsonschema -")
    def test_2(self, completion):
        assert completion
