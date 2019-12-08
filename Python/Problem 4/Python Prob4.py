import matplotlib.pyplot as plt
import numpy as np
h=float(input('Enter the initial height of the projectile above the ground in meters: '))
vel=float(input('Enter the magnitude of the velocity (m/s): '))
angle=float(input('Enter the angle in degrees with respect to the + X-axis at which the projectile is fired: '))
Xacc=float(input('Enter the X-COMPONENT of the acceleration, considering the sign (m/s^2): '))
Yacc=float(input('Enter the Y-COMPONENT of the acceleration, considering the sign (m/s^2): '))
if Yacc==0:
    print('Error: Vertical acceleration must not be zero')
    exit()
elif vel<0:
    print('Error: Magnitude of velocity cannot be less than zero')
    exit()
elif h<0:
    print('Error: Initial height MUST be above ground')
    exit()
time=(vel*(np.sin(np.deg2rad(angle)))+np.sqrt(((vel*(np.sin(np.deg2rad(angle))))**2)+2*(np.abs(Yacc)*h)))/np.abs(Yacc)
timevector=np.linspace(0,time,1000)
Heq=[Xacc/2,vel*(np.cos(np.deg2rad(angle))),0]
Veq=[Yacc/2,vel*(np.sin(np.deg2rad(angle))),h]
Hvec=np.polyval(Heq,timevector)
Vvec=np.polyval(Veq,timevector)
plt.plot(Hvec,Vvec)
plt.xlabel('Horizontal')
plt.ylabel('Vertical')
plt.title('Projectile Trajectory')