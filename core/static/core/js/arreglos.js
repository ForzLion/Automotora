


//declaracion de un arreglo

var nombres = ["juanito", "leopoldo", "jenny", "falcao", 2000];

for(i = 0; i < nombres.length;i++) {
    console.log(nombres[i]);
}


//foreach
nombres.forEach(function(item){
    console.log(item);
});

//JSON
//los json se componen de elemento clave y valor
var personas = [
    {
        "nombre": "deyanirah",
        "edad": 60,
        "sexo":false,
        "rut":"1.291.333-1"
    },
    {
        "nombre": "jesus",
        "edad": 33,
        "sexo":true,
        "rut":"999.999.999-1"
    },
    {
        "nombre": "lorenzo lamas",
        "edad": 90,
        "sexo":true,
        "rut":"1.111.111-1"
    }

]

personas.forEach(function(item) {
    console.log(item.nombre);
    console.log(item.edad);
    console.log(item.sexo);
    console.log(item.rut);
    console.log("-------------------");
});




