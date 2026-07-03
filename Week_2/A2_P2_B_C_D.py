import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Part (B) & (C)
true_val,_=quad(lambda x:np.exp(-x**2),0,1)
N_values=[10**2,10**3,10**4,10**5]
estimates=[]
errors=[]
for N in N_values:
    U=np.random.uniform(0,1,size=N)
    estimate=np.mean(np.exp(-U**2))
    estimates.append(estimate)
    error=np.abs(estimate-true_val)
    errors.append(error)
    print(f"N={N}|Estimate:{estimate:.6f}|Error:{error:.6f}")

# Part (D)
plt.plot(N_values,estimates,marker='o',label='Monte Carlo Estimate')
plt.axhline(true_val,color='red',linestyle='--',label='True Value')
plt.xlabel('N')
plt.ylabel('Estimate')
plt.legend()
plt.show()