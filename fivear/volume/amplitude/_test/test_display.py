"""

    *Amplitude - Display,   [Unit Tests]*

"""

from ..display import Display


class TestAmplitudeDisplay:
    def test_repr(self):
        ampl = Display(0.5)
        assert repr(ampl) == "0.500"
