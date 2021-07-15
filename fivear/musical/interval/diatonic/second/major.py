"""

    *Major 2nd*

  The major second interval of the diatonic scale.

    *Whole-Step*

  Also known as the whole step of the diatonic scale.

"""

from dataclasses import dataclass

from ...simple import SimpleInterval


@dataclass
class MajorSecond(
    SimpleInterval,
    Diatonic,
):
    pass
