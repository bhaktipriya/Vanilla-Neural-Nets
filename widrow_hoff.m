function [ a ] = widrow_hoff(Y , a, b, lr, theta)
n = size(Y,1);
iterations = 0;
all_pos =0;
while((all_pos ==0)&&(iterations<1000000))
    iterations = iterations+1; 
    fprintf('iteration=%d\n',iterations);
    all_pos = 1;
    for i = 1:n
        if(Y(i, :)*a'+b <=0)
            delta = lr*(Y(i,:))*((b(i)-Y(i,:)*a'));
            a = a + delta;
            if(abs(delta) > theta)
            all_pos = 0;
            end
            disp(a);
        end
    end
    if(all_pos==1)
        disp('haha');
    disp(a);
    end
end

