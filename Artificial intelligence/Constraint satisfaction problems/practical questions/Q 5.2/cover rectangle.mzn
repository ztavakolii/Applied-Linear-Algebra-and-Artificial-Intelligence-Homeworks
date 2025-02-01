include "alldifferent.mzn";
int:W;% width of big rectangle
int:H;% height of big rectangle
int:n; % number of small rectangles
array[1..n] of int: w; % w[i] is width of small rectangle i
array[1..n] of int: h; % h[i] is height of small rectangle i

array[1..n] of var 0..W:x; % x[i] is x coordinate of small rectangle i
array[1..n] of var 0..H:y;% y[i] is y coordinate of small rectangle i

constraint forall(i in 1..n)(
(x[i]+w[i]<=W)/\(y[i]+h[i]<=H)
);
constraint forall(i in 1..n,j in i+1..n)(
(x[i]+w[i]<=x[j]) \/ (x[j]+w[j]<=x[i]) \/ (y[i]+h[i]<=y[j]) \/ (y[j]+h[j]<=y[i])
);

solve satisfy;









