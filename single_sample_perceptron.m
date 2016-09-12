function [ a ] = single_sample_perceptron( Y , a, lr)
n = size(Y,1);
iterations = 0;
all_pos =0;
while((all_pos ==0) || (iterations<100000))
    iterations = iterations+1; 
    all_pos = 1;
    for i = 1:n
        if(Y(i, :)*a'<=0)
            a = a + lr*Y(i,:);
            all_pos = 0;
            disp(Y(i,:)*a');
        end
    end
    %disp(a);
end

