import math as m
x1=float(input('Enter the 1st X Value: '))
y1=float(input('Enter the 1st Y Value: '))
x2=float(input('Enter the 2nd X Value: '))
y2=float(input('Enter the 2nd Y Value: '))
x3=float(input('Enter the 3rd X Value: '))
y3=float(input('Enter the 3rd Y Value: '))
print('\n')
#operations for solving D, E,and F
X12=x1-x2
X13=x1-x3
X31=x3-x1
X21=x2-x1
Y12=y1-y2
Y13=y1-y3
Y31=y3-y1
Y21=y2-y1
X2X1=(x2**2)-(x1**2)
Y2Y1=(y2**2)-(y1**2)
X1X3=(x1**2)-(x3**2)
Y1Y3=(y1**2)-(y3**2)
#solving for D, E, and F
D=((X1X3*Y12)+(Y1Y3*Y12)+(X2X1*Y13)+(Y2Y1*Y13))/(2*((X31*Y12)-(X21*Y13)))#Is actually X
E=((X1X3*X12)+(Y1Y3*X12)+(X2X1*X13)+(Y2Y1*X13))/(2*((Y31*X12)-(Y21*X13)))#Is actually Y
F=-(x1**2)-(y1**2)-2*D*x1-2*E*y1
#For the center(h,k) and radius (r) of the circle
h=-D
k=-E
rroot=(h**2)+(k**2)-F
root=m.sqrt(rroot)
r=round(root,3)
print('Center:[',round(h,3),',',round(k,3),']')
print('Radius: ',round(r,3))
#GE:X**2+Y**2+2X+2Y+F, where X is D and Y is E
print('Vectors:[',round(2*D,3),round(2*E,3),round(F,3),']')