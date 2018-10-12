
//comentario de una linea
/*
comentario 
multilinea
*/
/*
var nombre = "juanito";
var edad = 20;
var sexo = true;

if(edad < 18) {
    alert("Es menor de edad"); 
} else {
    alert("Es mayor de edad");
}

for(i=0; i < 10; i++) {
    console.log(i);
}

var i = 0;

while(i < 20) {
    console.log("while " +i);
    i++;
}
*/

//$ significa jquery

$(document).ready(function() {
    //este codigo se ejecutara cuando ya todo el html esté cargado
    //obtenemos la caja completa

    //crearemos un listener para el event click del boton btnCalcular
    //para jquery el gato (#) significa que obtendremos el elemento por su id
    var btnCalcular = $("#btnCalcular");

    btnCalcular.click(function() {
         //el codigo que este aqui dentro se ejecutara
        //cuando se pinche el boton
        
        var txtNumero1 = $("#txtNumero1");
        var txtNumero2 = $("#txtNumero2");
        var txtResultado = $("#txtResultado");

        var tipoOperacion = $("#cboTipo").val();
        var resultado = 0;

        if(tipoOperacion == 1) {
            resultado 
            = parseInt(txtNumero1.val()) + parseInt(txtNumero2.val());
        } else if(tipoOperacion == 2) {
            resultado = 
            parseInt(txtNumero1.val()) - parseInt(txtNumero2.val());
        } else if(tipoOperacion == 3) {
            resultado = 
            parseInt(txtNumero1.val()) * parseInt(txtNumero2.val());
        } else {
            resultado =
            parseInt(txtNumero1.val()) / parseInt(txtNumero2.val());
        }

        txtResultado.val(resultado);
    });

});





