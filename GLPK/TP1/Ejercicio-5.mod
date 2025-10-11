#Ejercicio 5 Modelo 2

#Variable Decision
var x1 >= 0 , integer; 
var x2 >= 0, integer;
var x3 >= 0, integer;
var x4 >= 0, integer;
var y >= 0;

#Funcion Objetivo
maximize z: 60 * x1 + 45 * x2 + 130 * x3 + 90 * x4 - 40 * y;

#Restricciones
s.t. TBarriles: x1 + x2 == y;
s.t. CBarriles: y <= 20;
s.t. TiempoRef: 60 * x3 + 45 * x4 <= 480;
s.t. Control1: x1 - x2 <= 0;
s.t. Control2: x3 + x4 <= x1 + x2;
solve;

#Imprimime
display 'Total a Comprar: ' & y , 'CombAvion sin refinar: ' & (x1 - x3) ,
'Aceite sin refinar: ' & (x2 - x4) , 'CombAvion refinado: ' & x3 , 'Aceite refinado: ' & x4, 'Ganancias: ' & z;

end;
