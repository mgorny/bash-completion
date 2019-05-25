import pytest


class TestCppcheck:
    @pytest.mark.complete("cppcheck ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cppcheck -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("cppcheck -DFOO=BAR ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("cppcheck -D ")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("cppcheck --enable=al")
    def test_5(self, completion):
        assert completion == "--enable=all"

    @pytest.mark.complete("cppcheck --enable=xx,styl")
    def test_6(self, completion):
        assert completion == "--enable=xx,style"

    @pytest.mark.complete("cppcheck --enable=xx,yy,styl")
    def test_7(self, completion):
        assert completion == "--enable=xx,yy,style"
