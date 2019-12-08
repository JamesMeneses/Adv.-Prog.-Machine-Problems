function[] = matlab_MP_5()
clc
n = 0:199;
x = input('Enter function x(n):  ');
y = 0:199;

%--for the piecewise function y(n)--%
for counter = 1:1:200
    if counter == 1
        y(counter) = -1.5*x(counter) + 2*x(counter+1) -0.5*x(counter+2);
    elseif counter>1 && counter<=199
        y(counter) = 0.5*x(counter+1) -0.5*x(counter-1);
    elseif counter == 200
        y(counter) = 1.5*x(counter) -2*x(counter-1) +0.5*x(counter-2);
    end
end
plot(n,x,'linewidth',3)
hold on
plot(n,y,'linewidth',3)
legend('x(n)','y(n)')
grid on
hold off
end
