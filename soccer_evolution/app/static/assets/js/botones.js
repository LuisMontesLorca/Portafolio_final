
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
          mostrarAlerta(); 
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

$(document).ready(function() {
  $('.agregar-cancha').on('click', function() {
    updateCartCount();
    var hora_inicio = $('#hora_inicio').val();
    console.log('Hora de inicio:', hora_inicio);

    var hora_fin = $('#hora_fin').val();
    console.log('Hora de fin:', hora_fin);

    var datepicker = $('#datepicker').val();
    console.log('Fecha:', datepicker);

    if (hora_inicio === '' || hora_fin === '') {
      $('#modal_condicion').modal('show');
      $('#modal_condicion').on('click', '.close, .btn-secondary', function() {
        $('#modal_condicion').modal('hide');
      });
      return;
    }

    $('#modal_arrendar').modal('show');

    $('#confirmar-btn').on('click', function() {
      $('#modal_arrendar').modal('hide');

      var formData = {
        hora_inicio: hora_inicio,
        hora_fin: hora_fin,
        datepicker: datepicker
      };

      console.log("ESTA ES LA DATA: ", formData);

      $.ajax({
        url: '/arrendar',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function(response) {
          console.log(response);
          if(response.bandera==0)
          {
            $('#modal_arriendo_no_disponible').modal('show');
            $('#mensaje_no_arriendo').html('<p>' + response.mensaje + '</p>');
              // Cerrar la modal cuando se hace clic en el botón "OK" o en la "X" de cierre
              $('#modal_arriendo_no_disponible').on('click', '.close, .btn-secondary', function() {
                $('#modal_arriendo_no_disponible').modal('hide');

                window.location.reload()

              });
          }
          else{
            mostrarAlerta(); 
          }
          updateCartCount(); // Actualizar el número de productos en el carrito
        },
        error: function(error) {
          console.log('Error en el envío: ', error);
        }
      });
    });

    $('#modal_arrendar').on('click', '.close, .btn-secondary', function() {
      $('#modal_arrendar').modal('hide');
    });
  });

  // Función para actualizar el número de productos en el carrito
  function updateCartCount() {
    $.ajax({
      url: '/agregar_al_carrito',
      type: 'GET',
      success: function(response) {
        if (response.count_productos > 0)
        {
        console.log("logrado")
        var count_productos = response.count_productos;
        $('#cantidad-productos').text(count_productos);
        }
        else
        {
          
          $('#cantidad-productos').text('0');
        }
      },
      error: function(error) {
        console.log('Error al obtener el número de productos: ', error);
      }
    });
  }

  // Llamar a la función para actualizar el número de productos al cargar la página
  updateCartCount();
});



    /* BOTON AGREGAR */

