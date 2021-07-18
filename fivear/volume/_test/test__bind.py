"""

    *Volume, Bindings   [Unit Tests]*

"""

from .._bind import Amplitude
from .._bind import Decibel
from .._bind import Phon
from .._bind import Power

from .._bind import Volume

class TestVolume:
    def test_attributes(self):
        assert Volume.Amplitude == Amplitude
        assert Volume.Decibel == Decibel
        assert Ampl.Power == Power
        assert Ampl.Phon == Phon

        assert issubclass(Ampl.Amplitude, Ampl)
        assert issubclass(Ampl.Decibel, Ampl)
        assert issubclass(Ampl.Power, Ampl)
        assert issubclass(Ampl.Phon, Ampl)

    def test_decibel(self):
        db = Decibel(-10)

        assert isinstance(db, Decibel)
        assert isinstance(db, float)

    def test_power(self):
        pow = Power(-10)

        assert isinstance(pow, Power)
        assert isinstance(pow, float)

    def test_phon(self):
        phon = Phon(3)

        assert isinstance(phon, Phon)
        assert isinstance(phon, float)

    def test_hooks(self):
