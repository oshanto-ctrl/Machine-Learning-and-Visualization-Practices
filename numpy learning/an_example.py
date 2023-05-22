import numpy as np

arr = np.arange(15).reshape(3, 5)

print(arr)

print("arr's size   ", arr.size)
print("arr's type   ", type(arr))
print("arr's shape  ", arr.shape)
print("arr's dimension  ", arr.ndim)
print("arr's datatype   ", arr.dtype.name)
print("arr's item_size  ", arr.itemsize)


# b array
print()
print()
print()


b = np.array([
    [6, 7, 8],
    [7, 3, 0]
])
print("arry b\n", b)
print("b's type ", type(b))
print("b's shape    ", b.shape)
print("b's dimension ", b.ndim)

