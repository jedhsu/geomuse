"""

    *Decibel - Convert - From,   [Unit Tests]*

"""

from pytest import approx

from ..from_ import Amplitude
from ..from_ import Decibel

from ..from_ import From


class TestDecibelFrom:
    def test_from_decibel(self):
        ampl = Amplitude(0.3162276)

        assert From.from_amplitude(ampl) == approx(10)
        assert From.from_amplitude(ampl) == approx(Decibel(10))

    # def test_from_power(self):
    #     pow = Power(-10)

    #     assert From.from_power(pow) == approx(0.1)
    #     assert From.from_power(pow) == approx(Power(0.1))
