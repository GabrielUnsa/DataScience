#Ejercicio 1 TP1
var x1 >= 0;
var x2 >= 0;
maximize z : 1000 * x1 + 3000 * x2;
subject to dia: 3 * x1 + 2 * x2 <= 12;
subject to hora: 2 * x1 + 6 * x2 <= 24; 
solve; #resolveme
display x1, x2, z;
end; 
