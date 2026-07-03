import numpy as np
import matplotlib.pyplot as plt

# Part (B)
N_values=[10**2,10**3,10**4,10**5]
points={}
for N in N_values:
    x=np.random.uniform(-1,1,N)
    y=np.random.uniform(-1,1,N)
    points[N]=(x,y)

# Part (C)
estimates={}
for N in N_values:
    x,y=points[N]
    inside=(x**2+y**2)<=1
    estimates[N]=4*np.mean(inside)
    print(f"N={N}|Estimate:{estimates[N]:.5f}")

# Part (D)
x,y=points[10000]
inside=(x**2+y**2)<=1
outside=~inside
plt.figure(figsize=(6,6))
plt.scatter(x[outside],y[outside],color='red',s=1)
plt.scatter(x[inside],y[inside],color='blue',s=1)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.gca().set_aspect('equal')
plt.show()

# Part (E)
plt.plot(N_values,[estimates[N] for N in N_values],marker='o')
plt.axhline(np.pi,color='red')
plt.xscale('log')
plt.show()