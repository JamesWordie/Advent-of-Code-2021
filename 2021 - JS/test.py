import numpy as np
from numpy.random import default_rng

'''
darr = np.eye(3, 5)
print(darr)

darr1 = np.ones((3, 5))
print(darr1)

darr0 = np.zeros((3, 5))
print(darr0)

rand = default_rng(42).random((2,3))
print(rand)

darrind = np.indices((3, 5))
print(darrind)

x = np.arange(10)
print(x[-2])

y = np.arange(35).reshape(5, 7)

print(y)

x = np.array([[ 0,  1,  2],
              [ 3,  4,  5],
              [ 6,  7,  8],
              [ 9, 10, 11]])
rows = np.array([[0, 0],
                 [3, 3]], dtype=np.intp)
columns = np.array([[0, 2],
                    [0, 2]], dtype=np.intp)

print()
print(x, "x")
print(rows, "rows")
print(columns, "cols")
print(x[rows, columns])

print()
print("*" * 30)
print(np.ones((2, 3, 4), dtype=np.int16))

print("*" * 30)

b = np.arange(12).reshape(4, 3)     # 2d array
print(b)


from collections import Counter
tmp = Counter("Guten Morgen Rosa".split())
print()
print(tmp)
# Counter({'Guten': 1, 'Rosa': 1, 'morgen': 1})

tmp = Counter("Good morning, Rosa!".split())
print()
print(tmp)
# Counter({'Good': 1, 'Rosa!': 1, 'morning,': 1})

# tmp = Counter("Good morning, Rosa! How is your good morning been Rosa?".split())
# Counter({'Good': 1, 'morning,': 1, 'Rosa!': 1, 'How': 1, 'is': 1, 'your': 1, 'good': 1, 'morning': 1, 'been': 1, 'Rosa?': 1})

'''

from itertools import permutations
tmp2 = [" ".join(combo) for combo in permutations("Good morning Rosa!".split(), 3)]
print(tmp2)
