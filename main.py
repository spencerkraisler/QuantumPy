from quantum import Register, Qubit
import gates as op
from math import sqrt, e, pi

A = Qubit(1,2, norm=True)
B = Qubit(3,4, norm=True)

print(A)
reg = A.outer(B)
print(reg)
