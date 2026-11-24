import numpy as np 
# task 2.3.1
s = np.arange(5,55,5)
print(s)
print(s.shape)
print(s.dtype)

 
# task 2.3.2
zero = np.zeros((4,4))
zero.flat[::5]=1
print(zero)

 
# task 2.3.3
even = np.linspace(0,2*np.pi,20)
sin = np.sin(even)
print(sin)

 
# task 2.3.4
r = np.random.randint(10, 99, size=(3, 3))
print(r)

 
# task 2.3.5
checker = np.zeros((5,5),dtype=int)
print(checker)
checker[::2,::2]=1
checker[1::2,1::2]=1
print(checker)


