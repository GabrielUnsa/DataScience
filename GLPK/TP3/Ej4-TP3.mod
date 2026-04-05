#Ejercicio 4 TP3
#Declaracion de Variable
var x1 >= 0 binary;
var x2 >= 0 binary;
var x3 >= 0 binary;
var x4 >= 0 binary;
var x5 >= 0 binary;
var x6 >= 0 binary;

#Funcion Objetivo
minimize z: x1 + x2 + x3 + x4 + x5 + x6;

#Restricciones
s.t. r1: x1 + x2 >= 1;
s.t. r2: x1 + x2 + x6 >= 1;
s.t. r3: x3 + x4 >= 1;
s.t. r4: x4 + x3 + x5 >= 1;
s.t. r5: x5 + x4 + x6 >= 1;
s.t. r6: x6 + x2 + x5 >= 1;

solve;
display x1, x2, x3 , x4, x5, x6, z;
end;
