function[] = MP_4()
clc
format short g
height = input('Enter the initial height of the projectile ABOVE the ground in meters: ');
velocity = input('Enter the magnitude of the velocity in m/s: ');
theta = input('Enter the angle in degrees with respect to the + X-axis at which the projectile is fired: ');
x_acc = input('Enter the X-COMPONENT of the acceleration, considering the sign, in m/s^2: ');
y_acc = input('Enter the Y-COMPONENT of the acceleration, considering the sign, in m/s^2: ');

if y_acc ==0 
    error('Vertical acceleration must not be zero')
elseif velocity<0
    error('Magnitude of the velocity cannot be zero')
elseif height<0
    error('Initial height nust be from above ground')
end

time = ((velocity*sind(theta)) + sqrt((velocity*sind(theta))^2 + 2*abs(y_acc)*height))/abs(y_acc);
%ymax = ((velocity^2)*(sind(theta)^2))/2*abs(y_acc);
t_vector = linspace(0,time,1000);

horizontal_eqn = [(x_acc)/2, velocity*cosd(theta), 0];
vertical_eqn = [(y_acc)/2, velocity*sind(theta), height];

h_vector = polyval(horizontal_eqn,t_vector);
v_vector = polyval(vertical_eqn, t_vector);


plot(h_vector,v_vector)
grid on
xlabel('horizontal')
ylabel('vertical')
title('projectile trajectory')

end


