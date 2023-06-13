
/* AGREGAR PELOTAS */ 
$(document).ready(function() {
  $('.agregar-pelota').on('click', function() {
    
    var id_pelota = $(this).data('id_pelota');
    console.log('ID de la pelota:', id_pelota);
    
    var nombre_pelota = $(this).data('nombre_pelota');
    console.log('ID de la pelota:', nombre_pelota);
    var valor_pelota = $(this).data('valor_pelota');

    // Abrir la modal
    $('#modal').modal('show');

    // Manejar el evento de confirmación
    $('#confirmar-btn').on('click', function() {
      // Cerrar la modal
      $('#modal').modal('hide');

      // Enviar el formulario mediante AJAX
      var formData = {
        id_pelota: id_pelota,
        nombre_pelota: nombre_pelota,
        valor_pelota: valor_pelota
      };
      console.log ("ESTA ES LA DATA: " + formData)
      console.log(formData.id_pelota);
      $.ajax({
        url: '/pelotas',
        type: 'POST',
        contentType: 'application/json', // Configura el tipo de contenido como JSON
        data: JSON.stringify(formData),
        success: function(response) {
          // Manejar la respuesta del servidor
          console.log('Envío exitoso');
          // Puedes realizar acciones adicionales después de enviar los datos del formulario
        },
        error: function(error) {
          // Manejar los errores del servidor
          console.log('Error en el envío: ', error);
        }
      });
    });

    // Manejar el evento de cerrar modal al hacer clic en el botón "Cerrar" o "Cancelar"
    $('#modal').on('click', '.close, .btn-secondary', function() {
      // Cerrar la modal
      $('#modal').modal('hide');
    });
  });
});

/* AGREGAR CAMISETAS */ 

$(document).ready(function() {
  $('.agregar-camiseta').on('click', function() {
    
    var id_camiseta = $(this).data('id_camiseta');
    console.log('ID de la pelota:', id_camiseta);
    
    var nombre_camiseta = $(this).data('nombre_camiseta');
    console.log('ID de la pelota:', nombre_camiseta);
    var valor_camiseta = $(this).data('valor_camiseta');

    // Abrir la modal
    $('#modal').modal('show');

    // Manejar el evento de confirmación
    $('#confirmar-btn').on('click', function() {
      // Cerrar la modal
      $('#modal').modal('hide');

      // Enviar el formulario mediante AJAX
      var formData = {
        id_camiseta: id_camiseta,
        nombre_camiseta: nombre_camiseta,
        valor_camiseta: valor_camiseta
      };
      console.log ("ESTA ES LA DATA: " + formData)
      console.log(formData.id_camiseta);
      $.ajax({
        url: '/camisetas',
        type: 'POST',
        contentType: 'application/json', // Configura el tipo de contenido como JSON
        data: JSON.stringify(formData),
        success: function(response) {
          // Manejar la respuesta del servidor
          console.log('Envío exitoso');
          // Puedes realizar acciones adicionales después de enviar los datos del formulario
        },
        error: function(error) {
          // Manejar los errores del servidor
          console.log('Error en el envío: ', error);
        }
      });
    });

    // Manejar el evento de cerrar modal al hacer clic en el botón "Cerrar" o "Cancelar"
    $('#modal').on('click', '.close, .btn-secondary', function() {
      // Cerrar la modal
      $('#modal').modal('hide');
    });
  });
});

/* AGREGAR BEBIDAS */


/* AGREGAR CANCHAS */ 

$(document).ready(function() 
{
  $('.agregar-cancha').on('click', function() 
  {
    var hora_inicio = $('#hora_inicio').val();
    console.log('Hora de inicio:', hora_inicio);

    var hora_fin = $('#hora_fin').val();
    console.log('Hora de fin:', hora_fin);

    var datepicker = $('#datepicker').val();
    console.log('Fecha:', datepicker);

    if (hora_inicio === '' || hora_fin === '') {
     // alert('Por favor, completa los campos de hora inicio y hora fin.');
      $('#modal_condicion').modal('show');
      $('#modal_condicion').on('click', '.close, .btn-secondary', function() {
        // Cerrar la modal
        $('#modal_condicion').modal('hide');
      });
      return
    }
    // Abrir la modal
    $('#modal_arrendar').modal('show');

    // Manejar el evento de confirmación
    $('#confirmar-btn').on('click', function() 
    {
      // Cerrar la modal
      $('#modal_arrendar').modal('hide');

      // Enviar el formulario mediante AJAX
      var formData = 
      {
        hora_inicio: hora_inicio,
        hora_fin: hora_fin,
        datepicker: datepicker
      };

      console.log("ESTA ES LA DATA: ", formData);

      $.ajax({
        url: '/arrendar',
        type: 'POST',
        contentType: 'application/json', // Configura el tipo de contenido como JSON
        data: JSON.stringify(formData),
        success: function(response) 
        {
          // Manejar la respuesta del servidor
          console.log('Envío exitoso');
          // Puedes realizar acciones adicionales después de enviar los datos del formulario
        },
        error: function(error) 
        {
          // Manejar los errores del servidor
          console.log('Error en el envío: ', error);
        }
      });
    });
        // Manejar el evento de cerrar modal al hacer clic en el botón "Cerrar" o "Cancelar"
        $('#modal_arrendar').on('click', '.close, .btn-secondary', function() {
          // Cerrar la modal
          $('#modal_arrendar').modal('hide');
        });
   
      });
    });


