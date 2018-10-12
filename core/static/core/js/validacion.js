

$(document).ready(function() {
    $("#formularioAuto").validate({
        rules:{
            txtPatente:{
                required:true,
                minlength:3,
                maxlength:10
            },
            cboMarca:{
                required:true
            },
            txtAnio: {
                required:true,
                number:true,
                min:1950,
                max:2018
            }
        },
        messages:{
            txtPatente:{
                required:"Este campo es requerido",
                minlength:"Minimo 3 letras",
                maxlength:"Maximo 10 letras"
                //email:true
                //date:true
            },
            cboMarca:{
                required:"Seleccione una marca"
            }
        }
    });
});