grammar gcode;

start : expr | <EOF> ;

expr     : 'G00' 'X'x_cord=NUMBER 'Y'y_cord=NUMBER #fastPositionExpr
         | 'G01'  'X'x_cord=NUMBER 'Y'y_cord=NUMBER ('F'speed=NUMBER)? ('Z'color=COLOR)?#linInterpolateExpr
         | 'G02' degrees=NUMBER #circularClockwiseInterpolateExpr
         | 'G03' radius=NUMBER degrees=NUMBER #drawarcExpr
         ;
NUMBER : '('-')?'('0' .. '9') + ('.' ('0' .. '9') +)? ;
COLOR: 'blue' | 'red' | 'green' | 'yellow' | 'pink';
WS : [ \r\n\t]+ -> skip;
