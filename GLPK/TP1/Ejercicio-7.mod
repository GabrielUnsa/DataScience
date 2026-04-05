#Ejercicio 7 

#Variables
var x11 >= 0;
var x12 >= 0;
var x13 >= 0;
var x21 >= 0;
var x22 >= 0;
var x23 >= 0;
var x31 >= 0;
var x32 >= 0;
var x33 >= 0;

#Funcion Objetivo
maximize z: 400 * ( x11 + x12 + x13 ) + 650 * ( x21 + x22 + x23 ) + 320 * ( x31 + x32 + x33 );

#Restricciones (Sujeto a)

#Sujeto a la disponibilidad en m3
s.t. r11: 1.2 * x11 + 2.7 * x21 + 1.9 * x31 <= 1560;
s.t. r12: 1.2 * x12 + 2.7 * x22 + 1.9 * x32 <= 2870;
s.t. r13: 1.2 * x13 + 2.7 * x23 + 1.9 * x33 <= 1350;

#Sujeto a cantidad disponible de los quimicos
s.t. r21: x11 + x12 + x12 <= 4032;
s.t. r22: x21 + x22 + x22 <= 5300;
s.t. r23: x31 + x32 + x32 <= 3700;

#Sujeto a cantidad maxima en los tanques
s.t. r31: x11 + x21 + x31 <= 2350;
s.t. r32: x12 + x22 + x32 <= 2890;
s.t. r33: x13 + x23 + x33 <= 1980;

#Sujeto a equilibrio de avion
s.t. r41: x12 + x22 + x32 = 0.5 * ( x13 + x23 + x33 );
s.t. r42: x11 + x21 + x31 = 2 * ( x12 + x22 + x32 ) - 80;

solve;
display x11, x12, x13, x21, x22, x23, x31, x32, x33, z;
end;
