import numpy as np
import matplotlib.pyplot as plt

def func(sigma):
    # Part (B)
    S_0=100
    K=110
    N=100000
    Z=np.random.normal(0,1,N)
    S_T=S_0*np.exp(sigma*Z)

    # Part (C)
    payoffs=np.maximum(S_T-K,0)

    # Part (D)
    expected_payoff=np.mean(payoffs)
    print(f"Estimate:{expected_payoff:.4f}")

    # Part (E)
    plt.hist(S_T,bins=100,density=True)
    plt.xlabel('S_T')
    plt.show()

    # Part (F)
    plt.hist(payoffs,bins=100,density=True)
    plt.xlabel('Payoff')
    plt.show()

print("Sigma:0.2")
func(0.2)

# Part (G)
sigma_values=[0.1,0.3,0.5]
for sigma in sigma_values:
    print(f"Sigma:{sigma}")
    func(sigma)