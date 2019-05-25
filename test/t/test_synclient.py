import pytest


class TestSynclient:

    # synclient -l may error out with e.g.
    # "Couldn't find synaptics properties. No synaptics driver loaded?"
    @pytest.mark.complete("synclient ", xfail="! synclient -l &>/dev/null")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("synclient -")
    def test_2(self, completion):
        assert completion
