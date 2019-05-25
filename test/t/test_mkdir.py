import pytest


class TestMkdir:
    @pytest.mark.complete("mkdir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("mkdir ", cwd="shared/default")
    def test_2(self, completion):
        assert completion == ["bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.xfail  # TODO: why path in completion, basename in .output?
    @pytest.mark.complete("mkdir shared/default/foo.d/")
    def test_3(self, completion):
        assert completion.output == "foo"
        assert completion == [completion.output]
