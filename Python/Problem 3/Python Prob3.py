
import matplotlib.pyplot as plt
import numpy as np
import math as m
print('Sample input  MP_3(np.array([[1,2],[3,4],...))')
print('')
print('Wherein 1 and 3 are the  are the x-components and \n2 and 4 are the y- components of \nthe data points')
def MP_3(comp):
    x = comp[:,0]
    y = comp[:,1]
    least=m.inf
    for ctr in range(11):
        if ctr>=len(x):
            break
        p=np.polyfit(x,y,ctr)
        y2=np.polyval(p,x)
        e=y-y2
        errorvector_norm=np.linalg.norm(e)
        if errorvector_norm<least:
            least=errorvector_norm
            bestfit=p
    plt.title('Machine Problem: Problem 3')
    y3 = np.polyval(bestfit,x)
    plt.plot(x,y,'-o',label="Data points")
    plt.plot(x,y3,'-*',label="Best Fit Curve")
    plt.legend(loc="upper right")
    print('Coefficients of Best Fit Polynomial: ', bestfit)
