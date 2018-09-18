import numpy as np
from math import sqrt, e

# returns complex number in rect. form
def polar(mag, phase):
	return mag * e ** (1j * phase)

# measures the state of Q, thereby collapsing it
def measure(Q):
	return np.random.choice(range(Q.dim), p=(abs(Q.ket.T) ** 2).tolist()[0])

# a Qubit Register 
class Register:

	# Args:
		# bits: number of qubits in register
	def __init__(self, bits):
		self.bits = bits
		self.dim = 2 ** bits # dim. of register's ket vector 
		self.ket = np.zeros((self.dim, 1))
		self.ket[0][0] = 1 # auto set to 0-state

	def __getitem__(self, idx):
		return self.ket[idx][0]
	
	# nicely prints out probability amplitudes in dirac notation
		# of everything I made in this program, 
		# this method is my pride and glory
	def __str__(self):
		output = ""
		for i in range(self.dim - 1):
			base = bin(i)[2:]
			for j in range(self.bits - len(base)): base = "0" + base
			output += str(np.round(self[i], 3)) + "|" + base + "> + "
		base = bin(self.dim - 1)[2:]
		scalar = str(np.round(self[self.dim - 1], 3))
		output += scalar + "|" + base + ">"
		return output
	
	# returns a Qubit Register object using tensor product np.kron()
	def outer(self, S):
		# S can be a Register or Qubit
		T = Register(self.bits + S.bits)
		T.ket = np.kron(self.ket, S.ket)
		return T

	def toArray(self):
		qubits = []
		for i in range(self.bits):
			return 1

class Qubit (Register):

	# Args:
		# a: probability amplitude for |0> vector
		# b: probability amplitude for |1> vector 
		# norm: if true, a and b are normalized s.t. their inner product is 1
			# else, a and b are accepted as the actual probability amplitudes
	def __init__(self, a=1, b=0, norm=False):
		self.bits = 1
		self.dim = 2
		self.ket = np.array([[a],[b]])
		norm_value = np.linalg.norm(self.ket)

		# checking if norm equals 1
		if norm == False: 
			assert norm_value > .9995 and norm_value < 1.0005, "Error: Norm is not unital."
		
		# if norm == True, then inner product of a and b will become 1
		else: 
			a, b = a/norm_value, b/norm_value
			self.ket = np.array([[a],[b]])


