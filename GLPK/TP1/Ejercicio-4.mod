#Ejercicio 4 TP1
#ultimo modificado
var x >= 0;
var y >= 0;
minimize z : 0.85 * x + 1.10 * y;
s.t. proteinas: ( 9200 * x + 12000 * y ) >= 20000; 
s.t. carbohidratos: ( 2000 * x + 4000 * y ) >= 12000;
s.t. Fibras: ( 8000 * x + 14000 * y )  >= 22800;
s.t. vitA: ( 0.1 * x + 0.15 * y ) >= 2;
s.t. vitB: ( 0.15 * x + 0.2 * y ) >= 3;
s.t. hierro: ( 0.3 * x + 0.2 * y ) >= 5;
s.t. grasas: ( 15000 * x + 7000 * y ) <= 250000;
solve;
display x , y , z;
end;
