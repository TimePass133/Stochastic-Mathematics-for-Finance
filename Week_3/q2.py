import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm,norm

np.random.seed(0)

# Part (d)
S0=100.0
mu=0.07
sigma=0.2
T=1.0
N=500
n_paths=50000
dt=T/N

dW=np.random.normal(0,np.sqrt(dt),size=(n_paths,N))
S=np.zeros((n_paths,N+1))
S[:,0]=S0
for k in range(N):
    S[:,k+1]=S[:,k]+mu*S[:,k]*dt+sigma*S[:,k]*dW[:,k]
ST=S[:,-1]

log_mean=np.log(S0)+(mu-0.5*sigma**2)*T
log_std=sigma*np.sqrt(T)
x=np.linspace(ST.min(),ST.max(),300)

plt.figure(figsize=(8,4))
plt.hist(ST,bins=100,density=True,alpha=0.6,color='steelblue',label='Simulated $S_T$')
plt.plot(x,lognorm.pdf(x,log_std,scale=np.exp(log_mean)),'r-',lw=2,label='Theoretical log-normal density')
plt.xlabel('Terminal Stock Price $S_T$')
plt.ylabel('Density')
plt.title('Part (d): Terminal Stock Price Distribution')
plt.legend()
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/q_gbm_terminal_dist.png', dpi=150)
plt.show()

# Part (e)
emp_mean_ST=np.mean(ST)
emp_std_ST=np.std(ST,ddof=1)
theo_mean_ST=S0*np.exp(mu*T)
theo_std_ST=S0*np.exp(mu*T)*np.sqrt(np.exp(sigma**2*T)-1)

print("Part (e)")
print(f"Empirical Mean: {emp_mean_ST:.4f} | Theoretical Mean: {theo_mean_ST:.4f}")
print(f"Empirical Std:  {emp_std_ST:.4f} | Theoretical Std:  {theo_std_ST:.4f}\n")


# Part (f)
sigmas=[0.1,0.3,0.5]
K=110.0

print("--- Part (f) Results ---")
for sig in sigmas:
    S_f=np.zeros((n_paths,N+1))
    S_f[:,0]=S0
    for k in range(N):
        S_f[:,k+1]=S_f[:,k]+mu*S_f[:,k]*dt+sig*S_f[:,k]*dW[:,k]
    ST_f=S_f[:,-1]
    e_mean=np.mean(ST_f)
    e_std=np.std(ST_f,ddof=1)
    payoff=np.maximum(ST_f-K,0)
    exp_payoff=np.mean(payoff)
    print(f"Sigma={sig}: Emp Mean={e_mean:.4f}, Emp Std={e_std:.4f}, Exp Payoff={exp_payoff:.4f}")
print()


# Part (g)
log_returns=np.log(ST/S0)
emp_mean_lr=np.mean(log_returns)
emp_var_lr=np.var(log_returns,ddof=1)
theo_mean_lr=(mu-0.5*sigma**2)*T
theo_var_lr=(sigma**2)*T

print("Part (g)")
print(f"Emp Log-Return Mean: {emp_mean_lr:.6f} | Theoretical: {theo_mean_lr:.6f}")
print(f"Emp Log-Return Var:  {emp_var_lr:.6f} | Theoretical: {theo_var_lr:.6f}")

x_lr=np.linspace(log_returns.min(),log_returns.max(),300)

plt.figure(figsize=(8,4))
plt.hist(log_returns,bins=100,density=True,alpha=0.6,color='mediumseagreen',label='Simulated Log-Returns')
plt.plot(x_lr,norm.pdf(x_lr,theo_mean_lr,np.sqrt(theo_var_lr)),'r-',lw=2,label='Theoretical Normal Density')
plt.xlabel('Log-Return $\ln(S_T/S_0)$')
plt.ylabel('Density')
plt.title('Part (g): Log-Return Distribution')
plt.legend()
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/q_gbm_log_returns.png',dpi=150)
plt.show()