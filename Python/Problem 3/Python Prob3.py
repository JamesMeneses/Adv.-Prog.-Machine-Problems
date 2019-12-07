import matplotlib.pyplot as plt
import numpy as np
import math as m
X=[]
Y=[]
x=0
y=0
while x!=('end'):
    x=input('Enter components of X and enter "End" if done: ').lower()
    if x!='end':
        x=int(x)
        X.append(x)
while y!=('end'):
    y=input('Enter components of Y and Enter "End" if done: ').lower()  
    if y!=('end'):
        y=int(y)
        Y.append(y)
least=m.inf
for ctr in range(9):
    if ctr>=len(X):
        break
    p=np.polyfit(X,Y,ctr)
    Y2=np.polyval(p,X)
    e=Y-Y2
    errorvector_norm=np.linalg.norm(e)
    if errorvector_norm<least:
        least=errorvector_norm
        bestfit=p        
plt.title('Machine Problem: Problem 3')
Y3 = np.polyval(bestfit,X)
plt.plot(X,Y,'-o',label='Data points')
plt.plot(X,Y3,'-*',label='Best Fit')
plt.legend(loc="upper right")