import matplotlib.pyplot as plt
import numpy as np
import sys
h=float(input('Enter the initial height of the projectile above the ground in meters: '))
vel=float(input('Enter the magnitude of the velocity (m/s): '))
angle=float(input('Enter the angle in degrees with respect to the + X-axis at which the projectile is fired: '))
Xacc=float(input('Enter the X-COMPONENT of the acceleration, considering the sign (m/s^2): '))
Yacc=float(input('Enter the Y-COMPONENT of the acceleration, considering the sign (m/s^2): '))
if Yacc==0:
    sys.exit('Error: Vertical acceleration must not be zero')
elif vel<0:
    sys.exit('Error: Magnitude of velocity cannot be less than zero')
elif h<0:
    sys.exit('Error: Initial height MUST be above ground')
time=(vel*(np.sin(np.deg2rad(angle)))+np.sqrt(((vel*(np.sin(np.deg2rad(angle))))**2)+2*(np.abs(Yacc)*h)))/np.abs(Yacc)
timevector=np.linspace(0,time,1000)
#ideal time for the trajectory to hit the ground(gravity = -9.8)
Idealtime=(vel*(np.sin(np.deg2rad(angle)))+np.sqrt(((vel*(np.sin(np.deg2rad(angle))))**2)+2*(np.abs(-9.8)*h)))/np.abs(-9.8)
Idealtimevector=np.linspace(0,Idealtime,1000)
Heq=[Xacc/2,vel*(np.cos(np.deg2rad(angle))),0]
Veq=[Yacc/2,vel*(np.sin(np.deg2rad(angle))),h]
#ideal trajectory of the projectile(the only acceleration is gravity = -9.8)
IdealHeq=[vel*np.cos(np.deg2rad(angle)),0]
IdealVeq=[-4.9,vel*np.sin(np.deg2rad(angle)),h]
Hvec=np.polyval(Heq,timevector)
Vvec=np.polyval(Veq,timevector)
#vector for the ideal trajectory of the projectile
IdealHvec=np.polyval(IdealHeq,Idealtimevector)
IdealVvec=np.polyval(IdealVeq,Idealtimevector)
plt.plot(Hvec,Vvec,linewidth=2.2,label="Non-ideal Trajectory")
plt.plot(IdealHvec,IdealVvec,linewidth=2.2,label="Ideal Trajectory")
plt.xlabel('Horizontal')
plt.ylabel('Vertical')
plt.legend(loc="upper right")
plt.title('Projectile Trajectory')