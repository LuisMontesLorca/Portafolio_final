$(document).ready(function() {
    $('#btn_registrarse').on('click', function() {
        console.log("click")
        rut_usuario= document.getElementById("rut_usuario").value
        nombre_usuario= document.getElementById("nombre_usuario").value
        apellido_usuario= document.getElementById("apellido_usuario").value
        correo_usuario= document.getElementById("correo_usuario").value
        console.log("ESTE ES EL CORREO QUE PASAREMOS POR EL AJAX: ", correo_usuario)
        password_usuario= document.getElementById("password_usuario").value
        telefono_usuario= document.getElementById("telefono_usuario").value
        direccion_usuario= document.getElementById("direccion_usuario").value
        region_usuario= document.getElementById("region_usuario").value
        provincia_usuario= document.getElementById("provincia_usuario").value
        comuna_usuario= document.getElementById("comuna_usuario").value

        var formData = {
            rut_usuario: rut_usuario,
            nombre_usuario: nombre_usuario,
            apellido_usuario: apellido_usuario,
            correo_usuario:correo_usuario,
            password_usuario:password_usuario,
            telefono_usuario:telefono_usuario,
            direccion_usuario:direccion_usuario,
            region_usuario:region_usuario,
            provincia_usuario:provincia_usuario,
            comuna_usuario:comuna_usuario
          };
        $.ajax({
          url: '/registro',
          type: 'POST',
          contentType: 'application/json',
          data: JSON.stringify(formData),
          success: function(response) {
            console.log(response);
            if(response.bandera==0)
            {
                console.log("EL CORREO EXISTE")
                mostrarAlertaRegistro
            }
            else{
                
                mostrarAlertaBienvenido
                console.log("EL CORREO NO EXISTE")
              
            }

          },
          error: function(error) {
            console.log('Error en el envío: ', error);
          }
        });
      });
    })