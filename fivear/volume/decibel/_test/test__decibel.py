"""

    *Decibel   [Unit Tests]*

"""

import pytest
from pytest import approx

from .._decibel import Volume

from .._decibel import Decibel


class TestDecibel:
    def test_init(self):
        db = Decibel(-10.0)
        assert isinstance(db, Decibel)
        assert isinstance(db, Volume)
        assert isinstance(db, float)
        assert db == approx(-10.0)

        with pytest.raises(ValueError):
            Decibel(5)


# class TestValidate:
#     def test_validate(self):
#         assert _Validate_(0.5)
#         assert _Validate_(0.01)
#         assert _Validate_(0.99)

#         with pytest.raises(ValueError):
#             _Validate_(-0.5).validate()
#             _Validate_(2.0).validate()
