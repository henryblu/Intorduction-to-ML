
import numpy as np
# 1. Solve numerically and report the eigenvalues λi and column eigenvectors xi, where i ∈ {1, 2}. 
#    Normalise the eigenvectors to unit length (if necessary).
A = np.array([[1, 2], 
              [2, 3.14159]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Question 2.1")
print("------------")
print("eigenvalues:")
print(eigenvalues)
print("\neigenvectors:")
print(np.matrix(eigenvectors))
print()
# 2. verify that the eigenvectors are orthogonal
orthogonal = np.dot(eigenvectors[:, 0], eigenvectors[:, 1])
norms = np.linalg.norm(eigenvectors, axis=0)
print("Question 2.2")
print("------------")
print("dot product rounded to 5th didget (orthogonality check)", orthogonal.round(5))
print("Norms (normalization check):", norms)
print()
#3. Show, by performing the numerical matrix computation, that A satisfies the equation
new_A =np.zeros((2, 2))
for i in range(len(A)):
    eigenvalue_matrix = eigenvalues[i] * np.identity(2)
    new_A += np.dot(eigenvalue_matrix, 
                    eigenvectors[:, i].reshape(2, 1) * eigenvectors[:, i].reshape(1, 2))
print("Question 2.3")
print("------------")
print("Matrix A:")
print(np.matrix(A))
print()
print("Matrix remade A:")
print(np.matrix(new_A))
