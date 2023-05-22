import numpy as np

a = np.array([2, 3, 4])
# print(a)
# print(a.dtype)

"""
b = np.array([(1.1, 2.2, 3.3,
            (4, 5, 7))], dtype=int)
"""

c = np.array([
    [2, 4],
    [4, 5],
    [6, 7]
], dtype=int)

# print(c)
# print(c.dtype)
# print(c.ndim)

# create an array full of zeroes

z = np.zeros((4, 4), dtype=np.int32)
# print("\n", z, "\nz type", type(z), "\ndtype", z.dtype.name, "\nshp", z.shape)

o = np.ones((2, 3, 4), dtype=np.int16)
# print("ones\n", o)
# print("one's shape", o.shape)
# print("one's dimension", o.ndim)

# arange






















