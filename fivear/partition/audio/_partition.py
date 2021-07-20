"""

Partition audio values into absolute key classes.

Partition audio deltas into relative key classes.

Partition time values into absolute key classes (beat).

"""

# circ imports an issue later.. deal

from fivear.class_.audio import AudioClass


class AudioPartition(
    tuple[AudioClass],
):
    pass
