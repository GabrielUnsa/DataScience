#Ejercicio 13

#Declaracion Variable
var x1 >= 0;
var x2 >= 0;

#Funcion Objetivo
minimize z: 50 * x1 + 25 * x2;

#Restricciones (Sujeto a)
s.t. grasas: 0.1 * x1 + 0.3 * x2 >= 8;
s.t. carbohidratos: 0.3 * x1 + 0.4 * x2 >= 19;
s.t. calcio: 0.3 * x1 + 0.1 * x2 >= 7;

solve;
display x1, x2, z;
end;
