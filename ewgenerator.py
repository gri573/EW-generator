import numpy as np
import sys
from copy import deepcopy

def invert(A):
	n = len(A)
	Ainv = []
	for k in range(n):
		Ainv.append(np.zeros(n))
		Ainv[k][k] = 1
	for k in range(n):
		A[k] = np.array(A[k])
	# Diagonalnullen wegtauschen
		if A[k][k] == 0:
			i = n - 1
			while i > k:
				if A[i][k] != 0:
					Z = A[k]
					A[k] = A[i]
					A[i] = Z
					Z = Ainv[k]
					Ainv[k] = Ainv[i]
					Ainv[i] = Z
					i = -5
				i -= 1
		# Werte unterhalb des Diagonalelementes töten, Ergebnis anzeigen
		for i in range(n - k - 1):
			if A[i + k + 1][k] != 0:
				mult = A[i + k + 1][k] / A[k][k]
				A[i + k + 1] = np.array(A[i + k + 1]) - np.array(A[k]) * mult
				Ainv[i + k + 1] = np.array(Ainv[i + k + 1]) - np.array(Ainv[k]) * mult
	# Werte oberhalb der Diagonale töten
	for k in range(n):
		for i in range(n - k - 1):
			if A[i][n - k - 1] != 0:
				if A[n - k - 1][n - k - 1] != 0:
					mult = A[i][n - k - 1] / A[n - k - 1][n - k - 1]
				else:
					raise Exception("Matrix nicht invertierbar")
				A[i] = np.array(A[i]) - np.array(A[n - k - 1]) * mult
				Ainv[i] = np.array(Ainv[i]) - np.array(Ainv[n - k - 1]) * mult
	for k in range(n):
		if A[k][k] != 0:
			Ainv[k] /= A[k][k]
		else:
			raise Exception("Matrix nicht invertierbar")
	return np.array(Ainv)

def genDiagMat(n):
	A = []
	for k in range(n):
		A.append(np.zeros(n))
		A[k][k] = np.random.randint(-5, 6)
	return np.array(A)

def genRanMat(n):
	A = []
	for k in range(n):
		col = []
		for l in range(n):
			col.append(np.random.randint(-1, 2))
		A.append(np.array(col))
	return np.array(A)

def matrixMult(A, B):
	AB = []
	for k in range(len(B)):
		col = []
		for l in range(len(A[0])):
			val = 0
			for m in range(len(A)):
				val += A[m][l] * B[k][m]
			col.append(val)
		AB.append(np.array(col))
	return np.array(AB)

def printmat(A):
	for k in range(len(A)):
		printstring = "|"
		for l in range(len(A[0])):
			if A[l][k] >= 0:
				printstring += " "
			printstring += str(A[l][k]) + " "
		printstring += "|"
		print(printstring)

n = sys.argv[1]
n = int(n)
A0 = genDiagMat(n)
S = genRanMat(n)
working = False
while not working:
	try:
		Sinv = invert(deepcopy(S))
		working = True
	except:
		S = genRanMat(n)
A = matrixMult(Sinv, matrixMult(A0, S))
print("Diagonalisieren Sie bitte die folgende Matrix:")
printmat(A)
showEW = input("Eigenwerte anzeigen")
EW = ""
for k in range(n):
	EW += str(A0[k][k]) + "; "
print(EW)