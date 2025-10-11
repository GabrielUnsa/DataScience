#Ejercicio 9

#Variable Decision
var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;
var x5 >= 0;

#Funcion Objetivo
maximize z: 0.14 * x1 + 0.13 * x2 + 0.12 * x3 + 0.125 * x4 + 0.1 * x5;

#Sujeto a (Restricciones)
s.t. banca: x4 + x5 >= 4800000; 
s.t. vmax: x3 >= 0.5 * ( x1 + x2 + x3 );
s.t. riesgo: 0.1 * x1 + 0.07 * x2 + 0.03 * x3 + 0.05 * x4 + 0.02 * x5 <= 480000;
s.t. total: x1 + x2 +x3 + x4+ x5 <=12000000;

solve;
display x1, x2, x3, x4, x5, z;
end;
