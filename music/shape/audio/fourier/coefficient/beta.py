"""

Beta (B_n) coefficients of a Fourier series.

"""


from sympy import Function, pi


class _Beta:
    function = Function("((-1) ^ n) * ((2 * A) / (pi * n))")


class _Iterate_(_Beta):
    def __next__(self):
        ...

    def __iter__(self):
        return self


class _Display_(_Beta):
    def __repr__(self):
        return self.function


class Beta(_Iterate_):
    def __iter__(self):
        ...
