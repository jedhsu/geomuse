"""

    Frames

  Atomic type. Also known as sample.

"""

# remniscent of bytes

from numpy import ndarray  # TODO: take care of view array (possibly with internal pkg)

# -
# Frames are held in a container due to memory constraints.
# -


class _Frames:
    arr: ndarray


class Frames:
    """
    Returns a view of the underlying array.

    """

    ...
