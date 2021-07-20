"""

    *Twelfth Audio Partition*
    
  The twelfth audio partition.

  Common known as diatonic scale.

"""

from dataclasses import dataclass

from .._partition import AudioPartition

__all__ = ["Diatonic"]


@dataclass
class TwelvthAudioPartition(
    AudioPartition,
):
    def __init__(
        self,
    ):
        elements = 12
        super(Diatonic, self).__init__(
            elements,
        )

    def ratio(self):
        """
        2 root 12
        """

    def __get_item__(self):
        pass
