function [ a ] = widrow_hoff(Y , a, b, lr, theta)
n = size(Y,1);
iterations = 0;
all_pos =0;
while((all_pos==0)&&(iterations<1000000))
    iterations = iterations+1; 
    fprintf('iteration=%d\n',iterations);
    all_pos = 1;
    for i = 1:n
            if(isnan(b-Y(i,:)*a')||isinf(b-Y(i,:)*a'))
               all_pos=1
               break
            end
            delta = (lr/iterations)*(Y(i,:))*((b-Y(i,:)*a'));
            %a = a + delta;
            if(delta > theta) 
                a = a + delta;                
                %disp(delta)
                all_pos = 0;
            end
            %disp(a);
        
    end
    if(all_pos==1)
    disp(a);
    end
end

