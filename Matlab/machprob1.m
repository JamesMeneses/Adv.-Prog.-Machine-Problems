n = linspace(0,99);
y = linspace(0,99);

for z = 1:1:100
    s = z;
   while s>=11
       s= s-10;
   end
   if s ==10
       s
       y(z) = NaN
       continue
   end
    y(z) = (s.^2)-7;
end
stem(n,y)
title('Machine Problem 1')
xlabel('n(0-99)')
ylabel('f(n)')