"""

    Tone

  Set of pitches and amplitudes.

"""

from dataclasses import dataclass

from ear4.wave import Frequency

# class FrequencyRange(Enum):
#     SUB = "SUB"
#     BASS = "BASS"
#     LOWS = "LOWS"
#     MIDS = "MIDS"
#     HIGHS = "HIGHS"
#     PRESENCE = "PRESENCE"
#     BRILLIANCE = "BRILLIANCE"

@dataclass
class _Tone:
    frequency: Frequency


class _Tone_:
    def fundamental(pitch: Pitch):

class Tone:
    ...
