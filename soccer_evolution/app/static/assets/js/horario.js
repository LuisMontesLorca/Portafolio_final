$(document).ready(function() {
    $("#hora_inicio").change(function() {
        var horaInicio = document.getElementById("hora_inicio").value
        console.log(horaInicio)

        var formData = {
            horaInicio: horaInicio
            };
        console.log(formData.horaInicio);
        $.ajax({
          url: '/horario',
          type: 'POST',
          contentType: 'application/json', // Configura el tipo de contenido como JSON
          data: JSON.stringify(formData),
          success: function(response) {
            if (response!= '') {
                var selectHoraFin = document.getElementById("hora_fin");
            
                // Limpiar las opciones existentes en el select
                selectHoraFin.innerHTML = "";
            
                // Crear y agregar la nueva opción al select utilizando append
                $(selectHoraFin).append($('<option>', {
                  value: response,
                  text: response
                }));
              }
            else
            {

            }
            // Manejar la respuesta del servidor
  
            // Puedes realizar acciones adicionales después de enviar los datos del formulario
          },
          error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
      });

    });