import os

import pytest


class TestValgrind:

    # b: Assume we have at least bash that starts with b in PATH
    @pytest.mark.complete("valgrind b")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("valgrind -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("valgrind --tool=memche")
    def test_3(self, completion):
        assert "--tool=memcheck" in completion

    @pytest.mark.complete("valgrind --tool=helgrind --history-l")
    def test_4(self, completion):
        assert "--history-level=" in completion
        assert not completion.endswith(" ")

    @pytest.mark.complete(r"valgrind --log-file=v\ 0.log ./bin/", cwd="shared")
    def test_5(self, completion):
        expected = sorted(
            [
                "%s/"
                for x in os.listdir("shared/bin")
                if os.path.isdir("shared/bin/%s" % x)
            ]
            + [
                x
                for x in os.listdir("shared/bin")
                if os.path.isfile("shared/bin/%s" % x)
            ]
        )
        assert completion == expected
