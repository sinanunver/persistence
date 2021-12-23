# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()

# importing "bisect" for bisection operations

import numpy as np
from bisect import bisect_left
from hopcroftkarp import HopcroftKarp
import warnings

# initializing list
S = np.array([-1, 3, 5])

T = np.array([10,5])



DUL= np.abs(S[:,None]-S[None,:])

print(DUL)

np.unique



D = np.zeros((3, 6))

print(D)

D[0:3, 0:3] = DUL

D[0:3,3:6 ] =np.inf*np.ones((3,3))

print(D)


d = D.flatten()
print(d)


ds=np.sort(np.unique(d))[0:-1]


print(ds)

bdist = ds[-1]
idx = bisect_left(range(ds.size), int(ds.size / 2))
print(ds[idx])


S= np.array([0,1])

print(S)
