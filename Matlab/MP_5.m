function[] = MP_5()
clc
n = 0:199;
x = input('Enter function x(n):  ');
y = 0:199;

for counter = 1:1:200
    if counter == 1
        y(counter) = -1.5*x(counter) + 2*x(counter+1) -0.5*x(counter+2);
    elseif counter>1 && counter<199
        y(counter) = 0.5*x(counter+1) -0.5*x(counter-1);
    elseif counter == 199
        y(counter) = NaN;
    elseif counter == 200
        y(counter) = 1.5*x(counter) -2*x(counter-1) +0.5*x(counter-2);
    end
end
plot(n,x,'-o')
hold on
plot(n,y,'-*')
legend('x(n)','y(n)')
grid on
hold off
end
    
