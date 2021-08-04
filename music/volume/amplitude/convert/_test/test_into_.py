"""

    *Amplitude - Convert - Into,   [Unit Tests]*

"""

from pytest import approx

from ..into_ import Decibel
from ..into_ import Power

from ..into_ import Into


class TestAmplitudeInto:
    def test_into_decibel(self):
        ampl = Into(0.1)

        assert ampl.into_decibel() == approx(-20)
        assert ampl.into_decibel() == approx(Decibel(-20))

    def test_into_power(self):
        ampl = Into(0.1)
        assert ampl.into_power() == approx(-10)
        assert ampl.into_power() == approx(Power(-10))

    # def test_into_phon(self):
    #     pass
