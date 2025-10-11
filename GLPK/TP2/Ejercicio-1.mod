#Ejercicio N° 1

#Declaracion Variables

var x1 >= 0;
var x2 >= 0;
var h1 >= 0;
var e1 >= 0;
var h2 >= 0;
var e2 >= 0;

#Funcion Objetivo
minimize z: 15 * h1 + 30 * e2;

#Restricciones
s.t. RendAnual: 3 * x1 + 5 * x2 + h1 - e1 = 9000;
s.t. IndRiesgo: 0.5 * x1 + 0.25 * x2 + h2 - e2 = 700;
s.t. TotalInv: 25 * x1 + 50 * x2 <= 80000;

solve;
display x1, x2, h1, h2, e1, e2, z;
end;
