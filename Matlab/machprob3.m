function[] = machprob3()
x = input('Enter the x components of the data points enclosed in bracket and separated by a comma: ');
y = input('Enter the y components of the data points enclosed in bracket and separated by a comma: ');
least = inf;
format short g


for ctr =1:1:10
    if ctr >= length(x)
        continue
    end
    p = polyfit(x,y,ctr)
    y2 = polyval(p,x); 
    e = y-y2;
    errorvector_norm = norm(e)
    if errorvector_norm < least
        least = errorvector_norm
        ctr
        figure%
        plot(x,y,'-k')
        hold on;
        plot(x,y2,'--r')
        hold off;
    end
end
%fprintf('degree = %.4f',degree)