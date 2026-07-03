import random

simulations=10000

#Part(F)
observations=[]

for _ in range(simulations):
    if random.random()<0.20:
        I_B=1
        I_A=1 if random.random()<0.35 else 0
    else:
        I_B=0
        I_A=1 if random.random()<0.0375 else 0
    observations.append((I_A,I_B))

intersect=0
union=0
sum=0
sum_squared=0

for I_A,I_B in observations:
    if I_A==1 and I_B==1:
        intersect+=1
    if I_A==1 or I_B==1:
        union+=1
    N=I_A+I_B
    sum+=N
    sum_squared+=N**2

#Part (G)
prob_intersect=intersect/simulations
prob_union=union/simulations
expected_N=sum/simulations
expected_N_squared=sum_squared/simulations
var_N=expected_N_squared-(expected_N**2)

print(f"P(LA ∩ LB) Estimate: {prob_intersect:.4f}")
print(f"P(LA ∪ LB) Estimate: {prob_union:.4f}")
print(f"E[N] Estimate: {expected_N:.4f}")
print(f"Var(N) Estimate: {var_N:.4f}")