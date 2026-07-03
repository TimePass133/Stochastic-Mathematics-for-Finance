import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Part (C)
n_values=[10,50,200]
num=10000
Z_n_results={}
for n in n_values:
    samples=np.random.binomial(1,0.5,size=(num,n))
    S_n=np.sum(samples,axis=1)
    Z_n=(S_n-n/2)/np.sqrt(n/4)
    Z_n_results[n]=Z_n

# Part (D)
for n in n_values:
    Z=Z_n_results[n]
    plt.hist(Z,bins=50,density=True)
    plt.show()

# Part (E)
x=np.linspace(-4,4,1000)
for n in n_values:
    Z=Z_n_results[n]
    plt.hist(Z,bins=50,density=True)
    plt.plot(x,norm.pdf(x))
    plt.show()

# Part (G)
for n in n_values:
    Z_n=Z_n_results[n]
    emp_mean=np.mean(Z_n)
    emp_var=np.var(Z_n,ddof=1)
    print(f"n={n}|Mean:{emp_mean:.4f}|Variance:{emp_var:.4f}")