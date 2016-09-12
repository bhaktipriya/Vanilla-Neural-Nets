function [O] = parzen_window( A,h )

O = zeros(1,max(A));

n = size(A,2)
for i=1:max(A)
    for j=1:n
        fprintf('i=%d %d\n', i, A(j))
        if(abs((A(j)-i)/h)<=1/2)
        O(1,i) = O(1,i) + 1;
        end
        O(1,i)= O(i)/n;
        O(1,i)= O(i)/h;
    end
end

end

