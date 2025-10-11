#Ejercicio 10

#Declaracion Variables
var x1 >= 0;
var x2 >= 0;

#Funcion Objetivo
maximize z: 20 * x1 + 12 * x2;

#Restricciones(Sujeto a)
s.t. ensamblado: 90 * x1 + 30 * x2 <= 6000; #minutos
s.t. terminado: 60 * x1 + 30 * x2 <= 4800;

solve;
display x1, x2, z;
end;
