#Ejercicio 1 TP3
#Declaracion de Variable
var x1 >= 0 integer;
var x2 >= 0 integer;

#Funcion Objetivo
maximize z: x1 + 5 * x2;

#Restricciones
s.t. r1: x1 + 10 * x2 <= 20;
s.t. r2: x1 <= 2;
solve;
display x1, x2, z;
end;
