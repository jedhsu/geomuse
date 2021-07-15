"""

    *Amplitude   [Unit Tests]*

"""

import pytest

from .._amplitude import Amplitude


class TestAmplitude:
    def test_init(self):
        ampl = Amplitude(0.5)

        with pytest.raises(ValueError):
            Amplitude(-0.5)


# class TestValidate:
#     def test_validate(self):
#         assert _Validate_(0.5)
#         assert _Validate_(0.01)
#         assert _Validate_(0.99)

#         with pytest.raises(ValueError):
#             _Validate_(-0.5).validate()
#             _Validate_(2.0).validate()
