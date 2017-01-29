function [ a ] = perceptron_relaxation_margin(Y , a, b, lr)
n = size(Y,1);
iterations = 0;
all_pos =0;
while((all_pos ==0)&&(iterations<10000))
    iterations = iterations+1; 
    fprintf('iteration=%d\n',iterations);
    all_pos = 1;
    for i = 1:n
        if(Y(i, :)*a'+b <=0)
            %disp(lr*((b-Y(i,:)*a')/norm(Y(i,:))));
            a = a + (Y(i,:)*lr*((b-Y(i,:)*a')))/(norm(Y(i,:))*norm(Y(i,:)));
            all_pos = 0;
            %disp(a);
        end
    end
    if(all_pos==1)
        disp('haha');
    disp(a);
    end
end

