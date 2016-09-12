w1 = [2 7; 8, 1; 7, 5; 6, 3; 7, 8; 5, 9; 4, 5];
w2 = [4, 2; -1, -1; 1, 3; 3, -2; 5, 3.25; 2, 4; 7, 1 ];
w1_ = [ones(size(w1,1),1) w1];
w2_ = [ones(size(w2,1),1) w2];
w2_ = -w2_;

Y = [w1_;w2_];

a = [1 1 1]; 
b = [1 1 1];
color_mat = [ones(size(w1,1)) zeros(size(w2,1))];
O = single_sample_perceptron_margin(Y,a,b,1);

x = min([w1(:,1) ; w2(:,1)]):max([w1(:,1) ; w2(:,1)]);
y = O(1)/norm(O) + (O(2)*x)/O(3);
plot(w1(:,1),w1(:,2), 'g.',w2(:,1),w2(:,2), 'rs', x, y); 
