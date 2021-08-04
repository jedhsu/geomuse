"""

    *Amplitude - Convert - From,   [Unit Tests]*

"""

from pytest import approx

from ..from_ import Decibel
from ..from_ import Power
from ..from_ import Amplitude

from ..from_ import From


class TestAmplitudeFrom:
    def test_from_decibel(self):
        db = Decibel(-10)
        assert From.from_decibel(db) == approx(0.3162276)
        assert From.from_decibel(db) == approx(Amplitude(0.3162276))

    def test_from_power(self):
        pow = Power(-10)
        assert From.from_power(pow) == approx(0.1)
        assert From.from_power(pow) == approx(Power(0.1))
