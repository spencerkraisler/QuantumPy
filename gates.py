import numpy as np
from math import sqrt, log, pi, e
from quantum import Register

# a Quantum Logic Gate
# all custom quantum logic gates must be subclasses of the Gate object
class Gate:

	# Args:
		# M (matrix): matrix representation of quantum gate
	def __init__(self, matrix):
		assert matrix.shape[0] == matrix.shape[1], "Matrix is not square."
		self.M = matrix 

	def __call__(self, Q):

		# Register Q dim. must equal Gate dim.
		assert self.M.shape[0] == Q.ket.shape[0], "Matrices are not aligned."
		T = Register(int(log(Q.ket.shape[0]) / log(2)))
		T.ket = self.M.dot(Q.ket) 
		return T


class PhaseShiftGate(Gate):
	def __init__(self, phase):
		self.phase = phase
		self.M = np.array([[1, 0], [0, e ** (1j * self.phase)]])

H = Gate(matrix=(1.0 / sqrt(2)) * np.array([[1, 1], 
						  					[1, -1]]))
X = Gate(matrix=np.array([[0, 1],
						  [1, 0]]))
Y = Gate(matrix=np.array([[0, -1j], 
						  [1j, 0]]))
Z = PhaseShiftGate(pi)
R = PhaseShiftGate(pi/8)

SWAP = Gate(matrix=np.array([[1,0,0,0],
							 [0,0,1,0],
							 [0,1,0,0],
							 [0,0,0,1]]))


