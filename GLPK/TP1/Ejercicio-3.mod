#Ejercicio 3 TP1
var x1 >= 0;
var x2 >= 0;
maximize z : 46 * x1 + 76 * x2;
s.t. maximoHoras : 2 * x1 +  3 * x2 <= 60;
s.t. difDiversionEstudio : x1 + 2 * x2 <= 40;
solve;
display x1 , x2 , z;
end;