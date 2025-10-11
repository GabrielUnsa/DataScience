#Ejemplo de Practica
#Se aumento 5 en la primera restriccion
#Se aumento 5 en la segunda restriccion

#Declaracion de Variables
var x1 >= 0;
var x2 >= 0;

#Funcion objetivo
maximize z: 100 * x1 + 120 * x2;

#Restricciones
s.t. r1: 4 * x1 + 8 * x2 <= 565;
s.t. r2: 5 * x1 + 6 * x2 <= 610;
s.t. r3: 12 * x1 + 8 * x2 <= 570;

solve;
display x1, x2, z;
end;
#Resultado
#Aumento la ganancia pero a la vez el rango de actividad, por lo tanto 
#no podremos aconsejar porque al cambiar el rango es posible que la 
#empresa no tenga lo suficiente para dar mas mano de obra
