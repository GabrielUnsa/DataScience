#Ejercicio 6 TP1

#Variable Decision
var x1 >= 0;
var x2 >= 0;
var y1 >= 0;
var y2 >= 0;
var y3 >= 0;
var y >= 0;

#Funcion Objetivo
maximize z: 1500 * y - 110 * x1 - 120 * x2 - 130 * y1 - 110 * y2 - 115 * y3;

#Restricciones
s.t. vegetal : x1 + x2 <= 200;
s.t. oil: y1 + y2 + y3 <= 250;
s.t. total: x1+x2+y1+y2+y3 == y;
s.t. dureza: 8.8 * x1 +  6.1 * x2 + 2 * y1 + 4.2 * y2 + 5 * y3 <= 6 * y;
s.t. dureza2: 8.8 * x1 +  6.1 * x2 + 2 * y1 + 4.2 * y2 + 5 * y3 >= 3 * y; 
solve;
display 'Y:= ' & y , x1 , x2 , y1 , y2 , y3, z;
end;
