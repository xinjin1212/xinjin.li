yields=[[0.0418,0.0424,0.0417,0.0419,0.0427,0.0428,0.0428,0.0423,0.0424,0.0433],
        [0.0377,0.0380,0.0372,0.0377,0.0385,0.0386,0.0387,0.0382,0.0381,0.0395],
        [0.0355,0.0353,0.0344,0.0345,0.0354,0.0357,0.0360,0.0353,0.0352,0.0363],
        [0.0355,0.0353,0.0344,0.0345,0.0353,0.0357,0.0359,0.0351,0.0350,0.0361],
        [0.0339,0.0339,0.0328,0.0329,0.0337,0.0340,0.0342,0.0336,0.0335,0.0345],
        [0.0314,0.0310,0.0300,0.0298,0.0308,0.0311,0.0311,0.0306,0.0307,0.0317],
        [0.0316,0.0312,0.0300,0.0298,0.0310,0.0311,0.0311,0.0307,0.307,0.0316],
        [0.0305,0.0302,0.0289,0.0288,0.0299,0.0300,0.0300,0.0296,0.0297,0.0306],
        [0.0291,0.0288,0.0276,0.0276,0.0289,0.0289,0.0288,0.0285,0.0286,0.0296],
        [0.0283,0.0281,0.0296,0.0269,0.0281,0.0283,0.0283,0.0279,0.0281,0.0290]]

for i in range(10):
    exec(f"log_return_bond_{i+1} = np.array(yields[i])")
    
    exec(f"log_return_forward_{i+1} = np.array(F{i+1})")
num_obs = log_return_bond_1.shape[0]
log_returns = np.array([log_return_bond_1, log_return_bond_2, log_return_bond_3, log_return_bond_4,log_return_bond_5,log_return_bond_6,log_return_bond_7,log_return_bond_8,log_return_bond_9,log_return_bond_10])
covariance_matrix = (1 / (num_obs - 1)) * np.dot(log_returns, log_returns.T)##The np.dot() function is the dot-product of two arrays, np.dot(X.T, X) / n_samples, see the reference of COvariance Estimation.
print("The covariance matrix of log returns yield")
print(covariance_matrix)

log_returns_forward_rates = np.array([log_return_forward_1, log_return_forward_2, log_return_forward_3, log_return_forward_4,log_return_forward_5,log_return_forward_6,log_return_forward_7,log_return_forward_8,log_return_forward_9,log_return_forward_10])


covariance_matrix_forward_rates = (1 / (num_obs - 1)) * np.dot(log_returns_forward_rates, log_returns_forward_rates.T)
print("The covariance matrix of forward rates")
print(covariance_matrix_forward_rates)