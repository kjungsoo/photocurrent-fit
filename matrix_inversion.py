

# Implementation of what was in the handout on 2x2 matrix inversion is needed.

# The reason is that Newton's method in two dimensions involves inverting a
# 2x2 Hessian.


def invert_2x2(a, b, c, d):
    det = (a*d - b*c)
    if det != 0:
        e = d/det
        f = -b/det
        g = -c/det
        h = a/det
    else:
        e = a
        f = b
        g = c
        h = d
        print("Non-invertible matrix.")

    return e, f, g, h
