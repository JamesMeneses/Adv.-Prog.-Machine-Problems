import numpy as np
import matplotlib.pyplot as plt
n=np.arange(200)
print('Sample Input:  MP_5(np.sin((3*n*np.pi)/100))')
print('')
print('Wherein <np.sin((3*n*np.pi)/100)> is an array that is a function of n')
print('Please don''t forget to put the np prefix to the function to read the input as an array')
def MP_5(x):
    y=list(np.arange(200))
    for z in range(0,200):
        if z==0:
            y[z]= (-1.5*x[z]) + (2*x[z+1]) +(-0.5*x[z+2])
        elif z>0 and z<=198:
            y[z]=0.5*x[z+1] -0.5*x[z-1]
        elif z==199:
            y[z]=1.5*x[z] -2*x[z-1] +0.5*x[z-2]
                
    plt.plot(n,x,'-o',label="x(n)")
    plt.plot(n,y,'-',label="y(n)")
    plt.legend(loc="upper right")
    plt.grid(axis='both')
