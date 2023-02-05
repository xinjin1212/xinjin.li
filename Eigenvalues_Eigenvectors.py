eigenvalues1, eigenvectors1 = np.linalg.eig(covariance_matrix) #see referncence of np.linalg.eig in python.
print("Eigenvalues of log return yield :", eigenvalues1)
print("Eigenvectors of log return yield :", eigenvectors1)
eigenvalues2, eigenvectors2 = np.linalg.eig(covariance_matrix_forward_rates)
print("Eigenvalues of forward rates :", eigenvalues2)
print("Eigenvectors of forward rates :", eigenvectors2)