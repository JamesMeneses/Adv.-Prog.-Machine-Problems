import matplotlib.pyplot as plt
f=[]
n=[]
g=0
for i in range (100):
    n.append(i)
    x=i
    while x>=10:
        x=x-10
    if x<=9:
        g=(x**2)-7
        f.append(g)
    else:
        continue
plt.title('Machine Problem: Problem1')
plt.ylabel('f(n)')
plt.xlabel('n')
plt.stem(n,f)