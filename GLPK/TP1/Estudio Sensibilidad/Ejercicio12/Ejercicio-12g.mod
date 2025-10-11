#Ejercicio 12

#Declaracion Variable
var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;

#Funcion Objetivo
maximize z: 2 * x1 + 3 * x2 + 4 * x3 + 4 * x4;

#Restricciones (Sujeto a)
s.t. avellanas: x1 + x2 + 2 * x4 <= 500;
s.t. mani: x1 + 2 * x2 + x3 + x4 <= 1000;
s.t. chocolate: x1 + 2 * x3 + x4 <= 500;
s.t. limite: x3 <= 100;

solve;
display x1, x2, x3, z;
end;
