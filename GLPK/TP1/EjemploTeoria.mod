# MOD (modelo matematico)
# Ejemplo de Clase teorica
#variables (esto es un comentario)
var x1 >= 0;
var x2 >= 0;
maximize z : 100 * x1 + 200 * x2;
subject to has: x1 + x2 <= 80;
subject to agua: 0.8 * x1 + 2 * x2 <= 120; 
solve; #resolveme
display x1, x2, z;
#has es hectarias
end; 

# La instruccion para pasar el modelo matematico es glpsol -m uno.mod
# donde -m es modelo matematico