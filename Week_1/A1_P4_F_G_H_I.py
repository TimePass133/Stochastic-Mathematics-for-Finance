import random
import matplotlib.pyplot as plt

weeks=10000
state=0
P=[
    [0.60,0.30,0.10,0.00],
    [0.20,0.50,0.20,0.10],
    [0.10,0.30,0.40,0.20],
    [0.05,0.15,0.30,0.50]
]
returns=[0.012,0.004,-0.006,-0.025]
states=[0,1,2,3]

#Part (F)
path=[]
path_returns=[]

for _ in range(weeks):
    path.append(state)
    path_returns.append(returns[state])
    state=random.choices(states,weights=P[state],k=1)[0]

#Part (G)
counts=[path.count(i) for i in range(4)]
emp_pi=[c/weeks for c in counts]

print(f"Empirical pi: {[round(p,4) for p in emp_pi]}")

#Part (H)
emp_avg_ret=sum(path_returns)/weeks
print(f"Empirical Avg Return: {emp_avg_ret:.6f}")

#Part (I)
cum_ret=[]
current_sum=0
for r in path_returns:
    current_sum+=r
    cum_ret.append(current_sum)

plt.plot(cum_ret)
plt.title("Cumulative Portfolio Return over 10000 Weeks")
plt.xlabel("Weeks")
plt.ylabel("Cumulative Return")
plt.show()