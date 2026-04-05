#Ejercicio 8

#Variable Decision
var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;
var x5 >= 0;
var x6 >= 0;

#Funcion Objetivo
minimize z : x1 + x2 + x3 + x4 + x5 + x6;

#Sujetado a (Restricciones)
s.t. periodo1: x1 >= 20;
s.t. periodo2: x1 + x2 >= 50;
s.t. periodo3: x2 + x3 >= 80;
s.t. periodo4: x3 + x4 >= 100;
s.t. periodo5: x4 + x5 >= 40;
s.t. periodo6: x5 + x6 >= 30;
s.t. periodo7: x6 + x1 >= 20;

solve;
display x1, x2, x3, x4, x5, x6, z;
end;
