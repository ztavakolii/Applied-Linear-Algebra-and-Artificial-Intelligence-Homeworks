


% Use this editor as a MiniZinc scratch book
var float: y1;
var float: y2;
var float: y3;
var float: y4;
var float: y5;
var float: y6;

constraint y1 + 4 * y2 -2 * y4 - y5 <= y6;
constraint 5 * y1 -3 * y3 + 7 * y4 <= y6;
constraint -3 * y1 - y2 + 6 * y3 + 3 * y5 <= y6;
constraint -2 * y1 + 3 * y2 + y3 -4 * y4 -2 * y5 <= y6;
constraint 2 * y1 + y2 -4 * y3 - y4 <= y6;


constraint y1 + y2 + y3 + y4 + y5 = 1;

constraint y1 >= 0;
constraint y2 >= 0;
constraint y3 >= 0;
constraint y4 >= 0;
constraint y5 >= 0;

solve minimize y6;