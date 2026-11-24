import numpy as np

n=np.ones((4,3,2))
print(n)
print(n.ndim)
print(n.shape)
print(n.size)
print(n.nbytes)

n1=np.array([1,14,52],dtype=int)
print(n1.nbytes)
b=n1.astype(np.float32)
print(b.nbytes)

n2=np.array([1,56,20,62,14])
def describe(arr):
    print(arr.shape)
    print(arr.ndim)
    print(arr.size)
    print(arr.itemsize)
    print(arr.nbytes)
describe(n2)
            