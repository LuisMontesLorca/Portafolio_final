 // Función para actualizar el número de productos en el carrito
 function updateCartCount() 
 {
   $.ajax({
     url: '/agregar_al_carrito',
     type: 'GET',
     success: function(response) 
     {
      var count_productos=0
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
/* AGREGAR PELOTAS */ 
$(document).ready(function() {
  $('.agregar-pelota').on('click', function() {
    
    var id_pelota = $(this).data('id_pelota');
    console.log('ID de la pelota:', id_pelota);
    
    var nombre_pelota = $(this).data('nombre_pelota');
    console.log('ID de la pelota:', nombre_pelota);
    var valor_pelota = $(this).data('valor_pelota');
    var img_pelota = $(this).data('img_pelota');
    console.log('imagen de la pelota:', img_pelota);
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
        valor_pelota: valor_pelota,
        img_pelota:img_pelota
      };
      console.log ("ESTA ES LA DATA: " + formData)
      console.log(formData.id_pelota);
      $.ajax({
        url: '/pelotas',
        type: 'POST',
        contentType: 'application/json', // Configura el tipo de contenido como JSON
        data: JSON.stringify(formData),
        success: function(response) {
          if( response.bandera == 0)
          {
            updateCartCount(); 
            console.log('Envío exitoso');
            mostrarAlertaBalones(); 
          }else{
            updateCartCount(); 
            console.log('ERROR');
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
    var img_camiseta = $(this).data('img_camiseta');
    console.log('imagen de la pelota:', img_camiseta);

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
        valor_camiseta: valor_camiseta,
        img_camiseta:img_camiseta
      };
      console.log ("ESTA ES LA DATA: " + formData)
      console.log(formData.id_camiseta);
      $.ajax({
        url: '/camisetas',
        type: 'POST',
        contentType: 'application/json', // Configura el tipo de contenido como JSON
        data: JSON.stringify(formData),
        success: function(response) {
          if( response.bandera == 0)
          {
            updateCartCount(); 
            console.log('Envío exitoso');
            mostrarAlertaCamisetas();
            
          }else{
            console.log('ERROR');
            updateCartCount();
          }
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

$(document).ready(function() {
  $('.agregar-bebida').on('click', function() {
    
    var id_bebida = $(this).data('id_bebida');
    console.log('ID de la pelota:', id_bebida);
    
    var nombre_bebida = $(this).data('nombre_bebida');
    console.log('ID de la pelota:', nombre_bebida);
    var valor_bebida = $(this).data('valor_bebida');
    var img_bebida = $(this).data('img_bebida');
    // Abrir la modal
    $('#modal').modal('show');

    // Manejar el evento de confirmación
    $('#confirmar-btn').on('click', function() {
      // Cerrar la modal
      $('#modal').modal('hide');

      // Enviar el formulario mediante AJAX
      var formData = {
        id_bebida: id_bebida,
        nombre_bebida: nombre_bebida,
        valor_bebida: valor_bebida,
        img_bebida:img_bebida
      };
      console.log ("ESTA ES LA DATA: " + formData)
      console.log(formData.id_bebida);
      $.ajax({
        url: '/bebidas',
        type: 'POST',
        contentType: 'application/json', // Configura el tipo de contenido como JSON
        data: JSON.stringify(formData),
        success: function(response) {
          if( response.bandera == 0)
          {
            updateCartCount(); 
            console.log('Envío exitoso');
            mostrarAlertaBebidas();
          }
          else
          {
            updateCartCount();
            console.log('ERROR');
          }
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
    $('#modal').on('click', '.close, .btn-secondary', function() 
    {
      // Cerrar la modal
      $('#modal').modal('hide');
    });
  });
});

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

    if (hora_inicio === '' || hora_fin === '' || datepicker === '') 
    {
      $('#modal_condicion').modal('show');
      $('#modal_condicion').on('click', '.close, .btn-secondary', function() {
        $('#modal_condicion').modal('hide');
      });
      return;
    }

    $('#modal_arrendar').modal('show');

    $('#confirmar-btn').on('click', function() 
    {
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
        success: function(response) 
        {
          
          console.log(response);
          if(response.bandera==0)
          {


            $('#modal_arriendo_no_disponible').modal('show');
            $('#mensaje_no_arriendo').html('<p>' + response.mensaje + '</p>');
              // Cerrar la modal cuando se hace clic en el botón "OK" o en la "X" de cierre
              $('#modal_arriendo_no_disponible').on('click', '.close, .btn-secondary', function() 
              {
                $('#modal_arriendo_no_disponible').modal('hide');
                window.location.reload()
                updateCartCount()
              });
          }
          else
          {
            updateCartCount()
            mostrarAlertaArrendar(); 
           
          }
          // Actualizar el número de productos en el carrito
        },
        error: function(error) 
        {
          console.log('Error en el envío: ', error);
        }
      });
    });

    $('#modal_arrendar').on('click', '.close, .btn-secondary', function() 
    {
      $('#modal_arrendar').modal('hide');
    });
  });
});


        // ELIMINAR PRODUCTO DEL CARRO DE COMPRAS 

  $(document).ready(function() 
  {
    $('.eliminar-btn').click(function() 
    {
        var id_carro = $(this).data('id');
        var filaProducto = $(this).closest('tr');
  
        // Mostrar modal de confirmación
        $('#modal_eliminar_producto').modal('show');
  
        // Acción al hacer clic en cerrar o cancelar en el modal
        $('#modal_eliminar_producto').on('click', '.close, .btn-secondary', function() 
        {
            $('#modal_eliminar_producto').modal('hide');
        });
  
        // Acción al hacer clic en confirmar eliminar
        $('#btn_confirmar_eliminar').click(function() 
        {
            $.ajax({
                url: '/carro_compras/' + id_carro,
                type: 'DELETE',
                success: function(response) 
                {
                    // Eliminar la fila del producto
                    mostrarAlertaProductoEliminado()
                    updateCartCount();
                    filaProducto.remove();
                    window.location.reload()
                    
                },
                error: function(error) 
                {
                    console.log(error);
                }
            });
  
            // Ocultar el modal después de confirmar eliminar
            $('#modal_eliminar_producto').modal('hide');
        });
    });
  });








