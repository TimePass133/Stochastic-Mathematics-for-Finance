import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(0)

# Part (d)
X0=3.0
theta=2.0
sigma=0.5
T=5.0
N=5000
n_paths=10
dt=T/N
t=np.linspace(0,T,N+1)

plt.figure(figsize=(10,5))
for _ in range(n_paths):
    X=np.zeros(N+1)
    X[0]=X0
    for k in range(N):
        dW=np.random.normal(0,np.sqrt(dt))
        X[k+1]=X[k]-theta*X[k]*dt+sigma*dW
    plt.plot(t,X,alpha=0.5,linewidth=0.8)

stationary_std=sigma/np.sqrt(2*theta)
plt.axhline(0,color='black',linewidth=1.2,linestyle='--',label='Stationary mean = 0')
plt.fill_between(t,-2*stationary_std,2*stationary_std,alpha=0.1,color='red',label=r'$\pm 2\sigma/\sqrt{2\theta}$ band')
plt.xlabel('$t$')
plt.ylabel('$X_t$')
plt.title('Part (d): Ornstein-Uhlenbeck Paths')
plt.legend()
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/q_ou_paths.png',dpi=150)
plt.show()

# Part (e)
T_e=10.0
n_paths_e=20000
dt_e=T_e/N
dW_e=np.random.normal(0,np.sqrt(dt_e),size=(n_paths_e,N))
X_e=np.zeros((n_paths_e,N+1))
X_e[:,0]=X0

for k in range(N):
    X_e[:,k+1]=X_e[:,k]-theta*X_e[:,k]*dt_e+sigma*dW_e[:,k]
XT=X_e[:,-1]

theo_mean=0.0
theo_var=(sigma**2)/(2*theta)
emp_mean=np.mean(XT)
emp_var=np.var(XT,ddof=1)

print("Part (e)")
print(f"Empirical Mean: {emp_mean:.4f} | Theoretical Mean: {theo_mean:.4f}")
print(f"Empirical Var:  {emp_var:.4f} | Theoretical Var:  {theo_var:.4f}\n")

plt.figure(figsize=(8,4))
plt.hist(XT,bins=100,density=True,alpha=0.6,color='steelblue',label='Simulated $X_T$')
x_vals=np.linspace(XT.min(),XT.max(),300)
plt.plot(x_vals,norm.pdf(x_vals,theo_mean,np.sqrt(theo_var)),'r-',lw=2,label=r'Theoretical $\mathcal{N}(0, \sigma^2/(2\theta))$')
plt.xlabel('Terminal Value $X_T$')
plt.ylabel('Density')
plt.title('Part (e): Stationary Distribution Verification')
plt.legend()
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/q_ou_hist.png',dpi=150)
plt.show()

# Part (f)
thetas=[0.5,2.0,5.0]
fig,axs=plt.subplots(3,1,figsize=(8,10),sharex=True,sharey=True)

for i,th in enumerate(thetas):
    stat_std=sigma/np.sqrt(2*th)
    for _ in range(n_paths):
        X_f=np.zeros(N+1)
        X_f[0]=X0
        for k in range(N):
            dW_f=np.random.normal(0,np.sqrt(dt))
            X_f[k+1]=X_f[k]-th*X_f[k]*dt+sigma*dW_f
        axs[i].plot(t,X_f,alpha=0.5,linewidth=0.8)
    
    axs[i].axhline(0,color='black',linewidth=1.2,linestyle='--')
    axs[i].fill_between(t,-2*stat_std,2*stat_std,alpha=0.1,color='red')
    axs[i].set_title(f'$\\theta = {th}$')
    axs[i].grid(True,alpha=0.3)
    axs[i].set_ylabel('$X_t$')

axs[-1].set_xlabel('$t$')
plt.tight_layout()
plt.savefig('outputs/q_ou_thetas.png',dpi=150)
plt.show()