#Ejercicio 4 TP3
#Declaracion de Variable
var x1 >= 0 binary;
var x2 >= 0 binary;
var x3 >= 0 binary;
var x4 >= 0 binary;
var x5 >= 0 binary;
var x6 >= 0 binary;
var x7 >= 0 binary;

#Funcion Objetivo
minimize z: x1 + x2 + x3 + x4 + x5 + x6 + x7;

#Restricciones
s.t. A1: x1 + x2 + x3 + x4 + x5 >= 2;
s.t. A2: x2 + x4 + x5 + x6 >= 2;
s.t. A3: x3 + x6 + x7 >= 2;
s.t. C1: x4 <= x1;
s.t. C2: 2 * x7 <= x6 + x3;
s.t. C3: x5 <= x4;
solve;
display x1, x2, x3 , x4, x5, x6, x7, z;
end;
