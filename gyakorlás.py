import random
dobokockalista=[]
for i in range(0,10):
    dobokockalista.append(random.randint(1,6))
print(dobokockalista)
seged1=0
for i in range(0,len(dobokockalista),1):
    if dobokockalista[i]==6:
        seged1=seged1+1
print(f"a listában{seged1} darab 6 os szám szerepel")