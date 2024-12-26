grammar gcode;

start : expr | <EOF> ;

expr     : 'G00' 'X'x_cord=NUMBER 'Y'y_cord=NUMBER #fastPositionExpr
         | 'G01' 'X'x_cord=NUMBER 'Y'y_cord=NUMBER ('F'speed=NUMBER)? ('Z'color=COLOR)? #linInterpolateExpr
         | 'G02' degrees=NUMBER #circularClockwiseInterpolateExpr
         | 'G03' 'R'radius=NUMBER 'D'degrees=NUMBER ('F'speed=NUMBER)? ('Z'color=COLOR)? #drawarcExpr
         ;

R : 'R';
D : 'D';
F : 'F';
X : 'X';
Y : 'Y';
Z : 'Z';
NUMBER : '-'?('0' .. '9') + ('.' ('0' .. '9') +)? ;
COLOR: 'blue' | 'red' | 'green' | 'yellow' | 'pink';
WS : [ \r\n\t]+ -> skip;
