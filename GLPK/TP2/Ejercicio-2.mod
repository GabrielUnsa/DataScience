#Ejercicio N° 2

#Declaracion Variables

var x1 >= 0;
var x2 >= 0;
var h1 >= 0;
var h2 >= 0;
var h3 >= 0;
var h4 >= 0;
var e1 >= 0;
var e2 >= 0;
var e3 >= 0;
var e4 >= 0;

#Funcion Objetivo
minimize z: 200 * h1 + 100 * h2 + 50 * h3 + e4;

#Restricciones
s.t. Presupuesto: 100 * x1 + 60 * x2 + h4 - e4 = 600;
s.t. HAI: 7 * x1 + 3 * x2 + h1 - e1 = 40;
s.t. MAI: 5 * x1 + 4 * x2 + h2 - e2 = 60;
s.t. NIM: 10 * x1 + 5 * x2 + h3 - e3 = 35;

solve;
display x1, x2, h1, h2, h3, h4, e1, e2, e3, e4, z;
end;
