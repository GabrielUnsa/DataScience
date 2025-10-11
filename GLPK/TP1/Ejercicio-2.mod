#Ejercicio 2 TP1
var x1 >= 0;
var x2 >= 0;
maximize z : 2*x1 + x2;
s.t. maximoHoras : x1 + x2 <= 10;
s.t. difDiversionEstudio : x1 - x2 <= 1;
s.t. maximoDiversion : x1 <= 4;
solve;
display x1 , x2 , z;
end;