"""

    *Frequency Ratio*

  The frequency ratio of two pitches.

  # [TODO] equally tempered vs not?

"""

from fractions import Fraction

# [TODO] is this fraction or just value?


class FrequencyRatio(
    Fraction,
):
    def __init__(
        self,
        numerator: int,
        denominator: int,
    ):
        super(FrequencyRatio, self).__new__(
            Fraction,
            numerator,
            denominator,
        )
