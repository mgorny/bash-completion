import pytest


class TestTox:
    @pytest.mark.complete("tox -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tox -e ", cwd="tox")
    def test_2(self, completion):
        assert all(x in completion for x in "py37 ALL".split())

    @pytest.mark.complete("tox -e foo,", cwd="tox")
    def test_3(self, completion):
        assert all(x in completion for x in "py37 ALL".split())
