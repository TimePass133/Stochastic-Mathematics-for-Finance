import random

sims=1000
steps=100
state3_ct=0
class12_ct=0

P=[
    [0.60,0.25,0.05,0.10],
    [0.00,0.50,0.50,0.00],
    [0.00,0.50,0.50,0.00],
    [0.00,0.00,0.00,1.00]
]
states=[0,1,2,3]

#Part (G)
for _ in range(sims):
    state=0
    for _ in range(steps):
        if state==3:
            break
        state=random.choices(states,weights=P[state],k=1)[0]
    
    if state==3:
        state3_ct+=1
    elif state in (1,2):
        class12_ct+=1

#Part (H)
prop_3=state3_ct/sims
prop_12=class12_ct/sims

print(f"Proportion in State 3: {prop_3:.4f}")
print(f"Proportion in {{1, 2}}: {prop_12:.4f}")