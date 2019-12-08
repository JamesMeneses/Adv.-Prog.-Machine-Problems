function matlab_MP_1()
clc
n = linspace(0,99);
y = linspace(0,99);

for z = 1:1:100
    s = z-1;
   while s>=10
       s= s-10;
   end
    y(z) = (s.^2)-7;
end

stem(n,y)
title('Machine Problem 1')
xlabel({'n';'From 0-99'})
ylabel('f(n)') 
grid
end