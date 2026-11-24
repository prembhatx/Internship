import numpy as np

n=np.arange(5,55,5)
print(n)
print(n.shape)
print(n.dtype)

n1=np.zeros((4,4))
print(n1)
n1.flat[::5]=1
print(n1)

n2=np.linspace(0,2*np.pi,20)
print(n2)

n3=np.random.randint(10, 99, size=(3, 3))
print(n3)
print(n3.min())
print(n3.max())

n4=np.ones((5,5))
print(n4)
n4[::2, ::2]=0
n4[1::2, 1::2]=0
print(n4)

