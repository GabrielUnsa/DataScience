#Ejercicio 2 TP3
#Declaracion de Variable
var x1 >= 0 integer;
var x2 >= 0 integer;

#Funcion Objetivo
minimize z: 3 * x1 + 4 * x2;

#Restricciones
s.t. r1: x1 + 3 * x2 >= 40;
s.t. r2: x1 - x2 >= 5;
s.t. r3: 2 * x1 <= 31;
solve;
display x1, x2, z;
end;
