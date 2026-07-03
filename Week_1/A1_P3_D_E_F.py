import random

def simulate(d,paths,steps):
    #Part (D)
    returns=0
    origin=[0]*d
    for _ in range(paths):
        pos=[0]*d
        for _ in range(steps):
            dim=random.randrange(d)
            pos[dim]+=1 if random.random()<0.5 else -1
            if pos==origin:
                returns+=1
                break
    return returns/paths

#Part (E)
for d in [1,2,3]:
    print(f"d={d}: {simulate(d,1000,1000)}")

print("\n")

#Part (F)
for n in [100,1000,10000]:
    for d in [1,2,3]:
        print(f"d={d}, n={n}: {simulate(d,1000,n)}")