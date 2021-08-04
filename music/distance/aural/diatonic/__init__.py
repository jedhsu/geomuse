"""

    *mus . it . dia*

  The simple diatonic intervals.

"""

from .second import MinorSecond
from .second import MajorSecond
from .third import MinorThird
from .third import MajorThird
from .fourth import PerfectFourth
from .fifth import Tritone
from .fifth import PerfectFifth
from .sixth import MinorSixth
from .sixth import MajorSixth
from .seventh import MinorSeventh
from .seventh import MajorSeventh
from .eighth import Octave

__all__ = [
    "MinorSecond",
    "MajorSecond",
    "MinorThird",
    "MajorThird",
    "PerfectFourth",
    "Tritone",
    "PerfectFifth",
    "MinorSixth",
    "MajorSixth",
    "MinorSeventh",
    "MajorSeventh",
    "Octave",
]
