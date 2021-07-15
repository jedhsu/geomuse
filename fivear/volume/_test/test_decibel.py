import pytest

from ..decibel import Amplitude, Decibel, Power, _Validate_


class TestValidate:
    def test_validate(self):
        assert _Validate_(0.5)
        assert _Validate_(0.01)
        assert _Validate_(0.99)

        with pytest.raises(ValueError):
            _Validate_(-0.5).validate()
            _Validate_(2.0).validate()


class TestDisplay:
    def test_repr(self):
        db = Decibel(-20)

        assert repr(db) == "-20.00 db"


class TestFrom:
    def test_from_amplitude(self):
        ampl = Amplitude(0.25)

        assert Decibel.from_amplitude(ampl) == pprox(

    def test_from_power(self):
        db = Decibel.from_power(Power(-20))

        assert 1 == 2, db

    def test_from_phon(self):
        pass


class TestInto:
    def test_into_decibel(self):
        pass

    def test_into_power(self):
        pass

    def test_into_phon(self):
        pass


# class TestDecibel:
#     def test_init(self):
#         """
#         Tests for hooked validator

#         """

#         Amplitude(0.5)

#         with pytest.raises(ValueError):
#             Amplitude(-0.5)
