#Ejemplo de Practica
#Se agrego 5 a la restriccion 3

#Declaracion de Variables
var x1 >= 0;
var x2 >= 0;

#Funcion objetivo
maximize z: 100 * x1 + 120 * x2;

#Restricciones
s.t. r1: 4 * x1 + 8 * x2 <= 560;
s.t. r2: 5 * x1 + 6 * x2 <= 610;
s.t. r3: 12 * x1 + 8 * x2 <= 570;

solve;
display x1, x2, z;
end;
