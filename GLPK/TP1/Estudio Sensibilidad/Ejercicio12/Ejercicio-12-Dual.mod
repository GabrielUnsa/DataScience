#Ejercicio 12 Dual

#Declaracion Variable
var w1 >= 0;
var w2 >= 0;
var w3 >= 0;
var w4 >= 0;

#Funcion Objetivo
minimize y : 500 * w1 + 1000 * w2 + 500 * w3 + 100 * w4;

#Restricciones
s.t. r1: w1 + w2 + w3 >= 2;
s.t. r2: w1 + 2 * w2 >= 3;
s.t. r3: w2 + 2 * w3 + w4 >= 4;

solve;
display w1, w2, w3, w4, y;
end;
