import numpy as np



# Define Pauli matrices:
Pauli_x = np.array([[0, 1], [1, 0]])
Pauli_y = np.array([[0, -1j], [1j, 0]])
Pauli_z = np.array([[1, 0], [0, -1]])




print("The orginal square array of Pauli_x:\n", Pauli_x,"\n")


# Compute and print eigenvalues, eigenvectors and diagonal representation for Pauli_x:

val, vec = np.linalg.eig(Pauli_x)

print("The eigenvalue of Pauli_x:\n", val,"\n")

print("The eigenvector of Pauli_x:\n", vec,"\n")


diag = np.diag(val)

print("The diagonal representation of Pauli_x:\n", diag,"\n\n\n")

#########################################################################################

print("The orginal square array Pauli_y:\n", Pauli_y,"\n")


# Compute and print eigenvalues, eigenvectors and diagonal representation for Pauli_y:

val, vec = np.linalg.eig(Pauli_y)

print("The eigenvalue of Pauli_y:\n", val,"\n")

print("The eigenvector of Pauli_y:\n", vec,"\n")


diag = np.diag(val)

print("The diagonal representation of Pauli_y:\n", diag,"\n\n\n")

#########################################################################################

print("The orginal square array of Pauli_z:\n", Pauli_z,"\n")


# Compute and print eigenvalues, eigenvectors and diagonal representation for Pauli_z:

val, vec = np.linalg.eig(Pauli_z)

print("The eigenvalue of Pauli_z:\n", val,"\n")

print("The eigenvector of Pauli_z:\n", vec,"\n")


diag = np.diag(val)

print("The diagonal representation of Pauli_z:\n", diag,"\n")



print("Tap Enter Key to Exit.")
quit = input()