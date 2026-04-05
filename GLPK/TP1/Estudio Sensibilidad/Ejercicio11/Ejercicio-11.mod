#Ejercicio 11

#Variable Decision
var x1 >= 0;
var x2 >= 0;

#Funcion Objetivo
minimize z: 50000 * x1 + 100000 * x2;

#Restricciones (Sujeto a)
s.t. mujeres: 7 * x1 + 2 * x2 >= 28;
s.t. hombres: 2 * x1 + 12 * x2 >= 24;

solve;
display x1, x2, z;
end;
