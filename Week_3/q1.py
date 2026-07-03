import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Part (e)
T=1.0
N=10000
dt=T/N
dW=np.random.normal(0,np.sqrt(dt),size=N)
W=np.concatenate(([0],np.cumsum(dW)))
increments=np.diff(W)
QV=np.sum(increments**2)
TV=np.sum(np.abs(increments))

print("Part (e)")
print(f"Empirical Quadratic Variation: {QV:.6f}")
print(f"Theoretical Value T: {T:.6f}")
print(f"Difference: {abs(QV-T):.6f}")
print(f"Empirical Total Variation: {TV:.4f}\n")

# Part (f)
Ns=[10,50,100,500,1000,5000,10000]
qv_list=[]
for n in Ns:
    dt_n=T/n
    dW_n=np.random.normal(0,np.sqrt(dt_n),size=n)
    qv_n=np.sum(dW_n**2)
    qv_list.append(qv_n)

plt.figure(figsize=(8,4))
plt.semilogx(Ns,qv_list,'bo-',markersize=5,label='Empirical QV')
plt.axhline(T,color='black',linestyle='--',linewidth=1.5,label='True QV = 1')
plt.xlabel('Number of partition steps $N$ (Log Scale)')
plt.ylabel('Quadratic Variation')
plt.title('Convergence of Quadratic Variation to $T$ as Partition Refines')
plt.legend()
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/q_bm_qv_conv.png', dpi=150)
plt.show()

# Part (g)
n_paths=10000
N_g=1000
dt_g=T/N_g
dW_g=np.random.normal(0,np.sqrt(dt_g),size=(n_paths,N_g))
W_g=np.hstack([np.zeros((n_paths,1)),np.cumsum(dW_g,axis=1)])

t_fixed=0.5
t_index=int(t_fixed/dt_g)
W_t_samples=W_g[:,t_index]

empirical_mean=np.mean(W_t_samples)
empirical_variance=np.var(W_t_samples,ddof=1)

print("Part (g)")
print(f"Theoretical Mean: {0.0:.1f} | Empirical Mean: {empirical_mean:.4f}")
print(f"Theoretical Var: {t_fixed:.1f} | Empirical Var: {empirical_variance:.4f}")