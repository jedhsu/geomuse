"""

    *Tritone*

  The devil's interval.

  More precisely, the most dissonant of the diatonic intervals.

  Even more precisely, the diatonic interval that is least fractionally reducible
  on the frequency spectrum.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ..._interval import Interval


@dataclass
class Tritone(
    Interval,
    Diatonic,
):
    pass
