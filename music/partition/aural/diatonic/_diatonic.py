"""

    *Twelfth Aural Partition*

  The twelfth audio partition.

  Common known as diatonic scale.

"""

from dataclasses import dataclass

from .._partition import AuralPartition

__all__ = ["TwelfthAuraAuralition"]


@dataclass
class TwelfthAuralPartition(
    AuralPartition,
):
    def __init__(
        self,
    ):
        elements = 12
        super(TwelfthAuralPartition, self).__init__(
            elements,
        )

    def ratio(self):
        """
        2 root 12
        """

    def __get_item__(self):
        pass
