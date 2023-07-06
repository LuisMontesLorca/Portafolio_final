// abrir y cerrar modal
$(document).ready(function() 
{
    $('.agregar-cancha-futbol').on('click', function() 
    {
        $('#modal_agregar_cancha_futbol').modal('show')
        $('#modal_agregar_cancha_futbol').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_agregar_cancha_futbol').modal('hide');  
        });
    });
});
/* modal agregar cancha futbol*/ 
$(document).ready(function() 
{
    $('#btn_agregar_futbol').on('click', function() 
    {
        var nombre_cancha_futbol = document.getElementById('nombre_cancha_futbol').value;
        console.log('nombre de la cancha de futbol',nombre_cancha_futbol);

        var descripcion_cancha_futbol = document.getElementById('descripcion_cancha_futbol').value;
        console.log('descripcion de la cancha de futbol',descripcion_cancha_futbol);

        var valor_cancha_futbol = document.getElementById('valor_cancha_futbol').value;
        console.log('valor de la cancha de futbol',valor_cancha_futbol);

        if (nombre_cancha_futbol === '' || descripcion_cancha_futbol === '' ||valor_cancha_futbol === '') {
            // Mostrar mensaje de error
            alert('Por favor, rellene todos los campos');
            return; // Detener el envío del formulario
          }

          //envio formulario mediante AJAX
        var formData ={
            nombre_cancha_futbol: nombre_cancha_futbol,
            descripcion_cancha_futbol: descripcion_cancha_futbol, 
            valor_cancha_futbol: valor_cancha_futbol
        };
        console.log("aqui esta la data: " + formData)
        console.log(formData.descripcion_cancha_futbol);
        $.ajax({
            url: '/agregar_futbol',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                console.log('Envío exitoso');
                console.log(response.bandera);
                $('#modal_agregar_cancha_futbol').modal('hide');  
                document.getElementById('nombre_cancha_futbol').value=''
                document.getElementById('descripcion_cancha_futbol').value=''
                document.getElementById('valor_cancha_futbol').value=''
                window.location.href = "/lista_canchas";

   
        },
        error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
    })
});
        /* modal eliminar cancha futbol*/ 
        $(document).ready(function() 
        {
            $('.eliminar-canchafut-admin').on('click', function() 
            {
                $('#modal_eliminar_cancha_futbol').modal('show')
                $('#modal_eliminar_cancha_futbol').on('click', '.close, .btn-secondary',function() 
                {
                    // Cerrar la modal
                    $('#modal_eliminar_cancha_futbol').modal('hide');  
                });
            });
        });

        $(document).ready(function() {
            $('.eliminar-canchafut-admin').on('click', function() {
                var id_cancha_futbol = $(this).closest('tr').find('#id_cancha_futbol').val();
             console.log("id cancha futbol: ", id_cancha_futbol)
              // Abrir modal de confirmación
              $('#modal_eliminar_cancha_futbol').modal('show');
              
              // Manejar el click en el botón de eliminar dentro del modal
              $('#eliminar_canfut_btn').on('click', function() {
                // Envío de la solicitud de eliminación mediante AJAX
              $.ajax({
                url: '/eliminar_canfut_admin/' + id_cancha_futbol,
                type: 'DELETE',
                success: function(response) {
                    // Manejar la respuesta del servidor después de eliminar el producto
                    console.log(response);
                    window.location.reload();
                    
                },
                error: function(error) {
                    // Manejar el error si ocurre algún problema durante la solicitud AJAX
                    console.log(error);
                }
                
        });
                
                // Cerrar el modal después de enviar la solicitud
                $('#modal_eliminar_cancha_futbol').modal('hide');
            });
            });
        });
        
        /*MODAL EDITAR CANCHA FUTBOL*/ 
        
        $(document).ready(function() 
        {
            $('.editar-cancha-futbol-admin').on('click', function() 
            {
                console.log("click")
                $('#modal_editar_futbol').modal('show')
                $('#modal_editar_futbol').on('click', '.close, .btn-secondary',function() 
                {
                    // Cerrar la modal
                    $('#modal_editar_futbol').modal('hide');  
                });
            });
        });
        $(document).ready(function() {
            $('#btn_editar_futbol').on('click', function() {
                var id_cancha_futbol = document.getElementById('id_cancha_futbol_' + cancha_id).value;
                console.log("id cancha futbol: ", id_cancha_futbol); 
                // Envío de la solicitud de edición mediante AJAX
                var formData = {
                    id_cancha_futbol: id_cancha_futbol
                    
                };

                $.ajax({
                    url: '/editar_cancha_futbol_admin/' + id_cancha_futbol,
                    type: 'PUT',
                    contentType: 'application/x-www-form-urlencoded',
                    data: $.param(formData),
                    success: function(response) {
                        console.log('Envío exitoso');
                        
                    },
                    error: function(error) {
                        // Manejar el error si ocurre algún problema durante la solicitud AJAX
                        console.log('Error en el envío: ', error);
                    }
                });

            });
        });
        




  
        /* modal agregar cancha basket*/ 
// abrir y cerrar modal
$(document).ready(function() 
{
    $('.agregar-cancha-basket').on('click', function() 
    {
        $('#modal_agregar_cancha_basket').modal('show')
        $('#modal_agregar_cancha_basket').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_agregar_cancha_basket').modal('hide');  
        });
    });
});

$(document).ready(function() 
{
    $('#btn_agregar_basket').on('click', function() 
    {
        var nombre_cancha_basket = document.getElementById('nombre_cancha_basket').value;
        console.log('nombre de la cancha de basket',nombre_cancha_basket);

        var descripcion_cancha_basket = document.getElementById('descripcion_cancha_basket').value;
        console.log('descripcion de la cancha de basket',descripcion_cancha_basket);

        var valor_cancha_basket = document.getElementById('valor_cancha_basket').value;
        console.log('valor de la cancha de basket',valor_cancha_basket);

        if (nombre_cancha_basket === '' || descripcion_cancha_basket === '' ||valor_cancha_basket === '') {
            // Mostrar mensaje de error
            alert('Por favor, rellene todos los campos');
            return; // Detener el envío del formulario
          }

          //envio formulario mediante AJAX
        var formData ={
            nombre_cancha_basket: nombre_cancha_basket,
            descripcion_cancha_basket: descripcion_cancha_basket, 
            valor_cancha_basket: valor_cancha_basket
        };
        console.log("aqui esta la data: " + formData)
        console.log(formData.descripcion_cancha_basket);
        $.ajax({
            url: '/agregar_basket',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                console.log('Envío exitoso');
                console.log(response.bandera);
                $('#modal_agregar_cancha_basket').modal('hide');  
                document.getElementById('nombre_cancha_basket').value=''
                document.getElementById('descripcion_cancha_basket').value=''
                document.getElementById('valor_cancha_basket').value=''
                window.location.href = "/lista_canchas";

   
        },
        error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
    })
});

/* modal eliminar cancha basket*/ 
$(document).ready(function() 
{
    $('.eliminar-canchabasket-admin').on('click', function() 
    {
        $('#modal_eliminar_cancha_basket').modal('show')
        $('#modal_eliminar_cancha_basket').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_eliminar_cancha_basket').modal('hide');  
        });
    });
});

$(document).ready(function() {
    $('.eliminar-canchabasket-admin').on('click', function() {
        var id_cancha_basket = $(this).closest('tr').find('#id_cancha_basket').val();
     console.log("id cancha basket: ", id_cancha_basket)

      // Abrir modal de confirmación
      $('#modal_eliminar_cancha_basket').modal('show');
      
      // Manejar el click en el botón de eliminar dentro del modal
      $('#eliminar_canbasket_btn').on('click', function() {
        // Envío de la solicitud de eliminación mediante AJAX
      $.ajax({
        url: '/eliminar_canbasket_admin/' + id_cancha_basket,
        type: 'DELETE',
        success: function(response) {
            // Manejar la respuesta del servidor después de eliminar el producto
            console.log(response);
            window.location.reload();
            
        },
        error: function(error) {
            // Manejar el error si ocurre algún problema durante la solicitud AJAX
            console.log(error);
        }
        
});
        
        // Cerrar el modal después de enviar la solicitud
        $('#modal_eliminar_cancha_basket').modal('hide');
      });
    });
  });


 /* modal agregar cancha tenis*/ 
// abrir y cerrar modal
$(document).ready(function() 
{
    $('.agregar-cancha-tenis').on('click', function() 
    {
        $('#modal_agregar_cancha_tenis').modal('show')
        $('#modal_agregar_cancha_tenis').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_agregar_cancha_tenist').modal('hide');  
        });
    });
});

$(document).ready(function() 
{
    $('#btn_agregar_tenis').on('click', function() 
    {
        var nombre_cancha_tenis= document.getElementById('nombre_cancha_tenis').value;
        console.log('nombre de la cancha de tenis',nombre_cancha_tenis);

        var descripcion_cancha_tenis = document.getElementById('descripcion_cancha_tenis').value;
        console.log('descripcion de la cancha de tenis',descripcion_cancha_tenis);

        var valor_cancha_tenis = document.getElementById('valor_cancha_tenis').value;
        console.log('valor de la cancha de tenis',valor_cancha_tenis);

        if (nombre_cancha_tenis === '' || descripcion_cancha_tenis === '' ||valor_cancha_tenis === '') {
            // Mostrar mensaje de error
            alert('Por favor, rellene todos los campos');
            return; // Detener el envío del formulario
          }

          //envio formulario mediante AJAX
        var formData ={
            nombre_cancha_tenis: nombre_cancha_tenis,
            descripcion_cancha_tenis: descripcion_cancha_tenis, 
            valor_cancha_tenis: valor_cancha_tenis
        };
        console.log("aqui esta la data: " + formData)
        console.log(formData.descripcion_cancha_tenis);
        $.ajax({
            url: '/agregar_tenis',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                console.log('Envío exitoso');
                console.log(response.bandera);
                $('#modal_agregar_cancha_tenis').modal('hide');  
                document.getElementById('nombre_cancha_tenis').value=''
                document.getElementById('descripcion_cancha_tenis').value=''
                document.getElementById('valor_cancha_tenis').value=''
                window.location.href = "/lista_canchas";

   
        },
        error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
    })
});

/* modal eliminar cancha tenis*/ 
$(document).ready(function() 
{
    $('.eliminar-canchatenis-admin').on('click', function() 
    {
        $('#modal_eliminar_cancha_tenis').modal('show')
        $('#modal_eliminar_cancha_tenis').on('click', '.close, .btn-secondary',function() 
        {
             // Cerrar la modal
            $('#modal_eliminar_cancha_tenis').modal('hide');  
        });
    });
});

$(document).ready(function() {
    $('.eliminar-canchatenis-admin').on('click', function() {
        var id_cancha_tenis = $(this).closest('tr').find('#id_cancha_tenis').val();
    console.log("id cancha tenis: ", id_cancha_tenis)
       // Abrir modal de confirmación
    $('#modal_eliminar_cancha_tenis').modal('show');
    
       // Manejar el click en el botón de eliminar dentro del modal
    $('#eliminar_cantenis_btn').on('click', function() {
         // Envío de la solicitud de eliminación mediante AJAX
    $.ajax({
        url: '/eliminar_cantenis_admin/' + id_cancha_tenis,
        type: 'DELETE',
        success: function(response) {
             // Manejar la respuesta del servidor después de eliminar el producto
            console.log(response);
            window.location.reload();
            
        },
        error: function(error) {
             // Manejar el error si ocurre algún problema durante la solicitud AJAX
            console.log(error);
        }
        
});
        
         // Cerrar el modal después de enviar la solicitud
        $('#modal_eliminar_cancha_tenis').modal('hide');
    });
    });
});


/* modal agregar camiseta*/ 
// abrir y cerrar modal
$(document).ready(function() 
{
    $('.agregar-camiseta-admin').on('click', function() 
    {
        $('#modal_agregar_camiseta').modal('show')
        $('#modal_agregar_camiseta').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_agregar_camiseta').modal('hide');  
        });
    });
});

$(document).ready(function() 
{
    $('#btn_agregar_camiseta').on('click', function() 
    {
        var sku_camiseta= document.getElementById('sku_camiseta').value;
        console.log('sku de la camiseta',sku_camiseta);

        var nombre_camiseta= document.getElementById('nombre_camiseta').value;
        console.log('nombre de la camiseta',nombre_camiseta);

        var descripcion_camiseta = document.getElementById('descripcion_camiseta').value;
        console.log('descripcion de la camiseta',descripcion_camiseta);

        var valor_camiseta = document.getElementById('valor_camiseta').value;
        console.log('valor de la camiseta',valor_camiseta);

        if (sku_camiseta === '' || nombre_camiseta === '' || descripcion_camiseta === '' || valor_camiseta === '') {
            // Mostrar mensaje de error
            alert('Por favor, rellene todos los campos');
            return; // Detener el envío del formulario
          }

          //envio formulario mediante AJAX
        var formData ={
            sku_camiseta: sku_camiseta,
            nombre_camiseta: nombre_camiseta,
            descripcion_camiseta: descripcion_camiseta, 
            valor_camiseta: valor_camiseta
        };
        console.log("aqui esta la data: " + formData)
        console.log(formData.descripcion_camiseta);
        $.ajax({
            url: '/agregar_camiseta',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                console.log('Envío exitoso');
                console.log(response.bandera);
                $('#modal_agregar_camiseta').modal('hide');  
                document.getElementById('sku_camiseta').value=''
                document.getElementById('nombre_camiseta').value=''
                document.getElementById('descripcion_camiseta').value=''
                document.getElementById('valor_camiseta').value=''
                window.location.href = "/lista_canchas";

   
        },
        error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
    })
});

/* modal eliminar camiseta*/ 
$(document).ready(function() 
{
    $('.eliminar-camiseta-admin').on('click', function() 
    {
        $('#modal_eliminar_camiseta_admin').modal('show')
        $('#modal_eliminar_camiseta_admin').on('click', '.close, .btn-secondary',function() 
        {
             // Cerrar la modal
            $('#modal_eliminar_camiseta_admin').modal('hide');  
        });
    });
});

$(document).ready(function() {
    $('.eliminar-camiseta-admin').on('click', function() {
        var id_camiseta = $(this).closest('tr').find('#id_camiseta').val();
    console.log("id camiseta: ", id_camiseta)

       // Abrir modal de confirmación
    $('#modal_eliminar_camiseta_admin').modal('show');
    
       // Manejar el click en el botón de eliminar dentro del modal
    $('#eliminar_camiseta_btn').on('click', function() {
         // Envío de la solicitud de eliminación mediante AJAX
    $.ajax({
        url: '/eliminar_camiseta_admin/' + id_camiseta,
        type: 'DELETE',
        success: function(response) {
             // Manejar la respuesta del servidor después de eliminar el producto
            console.log(response);
            window.location.reload();
            
        },
        error: function(error) {
             // Manejar el error si ocurre algún problema durante la solicitud AJAX
            console.log(error);
        }
        
});
        
         // Cerrar el modal después de enviar la solicitud
        $('#modal_eliminar_camiseta_admin').modal('hide');
    });
    });
});

/* modal agregar pelota*/ 
// abrir y cerrar modal
$(document).ready(function() 
{
    $('.agregar-pelota-admin').on('click', function() 
    {
        $('#modal_agregar_pelota').modal('show')
        $('#modal_agregar_pelota').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_agregar_pelota').modal('hide');  
        });
    });
});

$(document).ready(function() 
{
    $('#btn_agregar_pelota').on('click', function() 
    {
        var sku_pelota= document.getElementById('sku_pelota').value;
        console.log('sku de la pelota',sku_pelota);

        var nombre_pelota= document.getElementById('nombre_pelota').value;
        console.log('nombre de la pelota',nombre_pelota);

        var descripcion_pelota = document.getElementById('descripcion_pelota').value;
        console.log('descripcion de la pelota',descripcion_pelota);

        var valor_pelota = document.getElementById('valor_pelota').value;
        console.log('valor de la pelota',valor_pelota);

        if (sku_pelota === '' || nombre_pelota === '' || descripcion_pelota === '' || valor_pelota === '') {
            // Mostrar mensaje de error
            alert('Por favor, rellene todos los campos');
            return; // Detener el envío del formulario
          }

          //envio formulario mediante AJAX
        var formData ={
            sku_pelota: sku_pelota,
            nombre_pelota: nombre_pelota,
            descripcion_pelota: descripcion_pelota, 
            valor_pelota: valor_pelota
        };
        console.log("aqui esta la data: " + formData)
        console.log(formData.descripcion_pelota);
        $.ajax({
            url: '/agregar_pelota',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                console.log('Envío exitoso');
                console.log(response.bandera);
                $('#modal_agregar_pelota').modal('hide');  
                document.getElementById('sku_pelota').value=''
                document.getElementById('nombre_pelota').value=''
                document.getElementById('descripcion_pelota').value=''
                document.getElementById('valor_pelota').value=''
                window.location.href = "/lista_canchas";

   
        },
        error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
    })
});

/* modal eliminar pelota*/ 
$(document).ready(function() 
{
    $('.eliminar-pelota-admin').on('click', function() 
    {
        $('#modal_eliminar_pelota_admin').modal('show')
        $('#modal_eliminar_pelota_admin').on('click', '.close, .btn-secondary',function() 
        {
             // Cerrar la modal
            $('#modal_eliminar_pelota_admin').modal('hide');  
        });
    });
});

$(document).ready(function() {
    $('.eliminar-pelota-admin').on('click', function() {
        var id_pelota = $(this).closest('tr').find('#id_pelota').val();
    console.log("id pelota: ", id_pelota)
    
       // Abrir modal de confirmación
    $('#modal_eliminar_pelota_admin').modal('show');
    
       // Manejar el click en el botón de eliminar dentro del modal
    $('#eliminar_pelota_btn').on('click', function() {
         // Envío de la solicitud de eliminación mediante AJAX
    $.ajax({
        url: '/eliminar_pelota_admin/' + id_pelota,
        type: 'DELETE',
        success: function(response) {
             // Manejar la respuesta del servidor después de eliminar el producto
            console.log(response);
            window.location.reload();
            
        },
        error: function(error) {
             // Manejar el error si ocurre algún problema durante la solicitud AJAX
            console.log(error);
        }
        
});
        
         // Cerrar el modal después de enviar la solicitud
        $('#modal_eliminar_pelota_admin').modal('hide');
    });
    });
});

/* modal agregar bebida*/ 
// abrir y cerrar modal
$(document).ready(function() 
{
    $('.agregar-bebida-admin').on('click', function() 
    {
        $('#modal_agregar_bebida').modal('show')
        $('#modal_agregar_bebida').on('click', '.close, .btn-secondary',function() 
        {
            // Cerrar la modal
            $('#modal_agregar_bebida').modal('hide');  
        });
    });
});

$(document).ready(function() 
{
    $('#btn_agregar_bebida').on('click', function() 
    {
        var sku_bebida= document.getElementById('sku_bebida').value;
        console.log('sku de la bebida',sku_bebida);

        var nombre_bebida= document.getElementById('nombre_bebida').value;
        console.log('nombre de la bebida',nombre_bebida);

        var descripcion_bebida = document.getElementById('descripcion_bebida').value;
        console.log('descripcion de la bebida',descripcion_bebida);

        var valor_bebida = document.getElementById('valor_bebida').value;
        console.log('valor de la bebida',valor_bebida);

        if (sku_bebida === '' || nombre_bebida === '' || descripcion_bebida === '' || valor_bebida === '') {
            // Mostrar mensaje de error
            alert('Por favor, rellene todos los campos');
            return; // Detener el envío del formulario
        }

          //envio formulario mediante AJAX
        var formData ={
            sku_bebida: sku_bebida,
            nombre_bebida: nombre_bebida,
            descripcion_bebida: descripcion_bebida, 
            valor_bebida: valor_bebida
        };
        console.log("aqui esta la data: " + formData)
        console.log(formData.descripcion_bebida);
        $.ajax({
            url: '/agregar_bebida',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                console.log('Envío exitoso');
                console.log(response.bandera);
                $('#modal_agregar_bebida').modal('hide');  
                document.getElementById('sku_bebida').value=''
                document.getElementById('nombre_bebida').value=''
                document.getElementById('descripcion_bebida').value=''
                document.getElementById('valor_bebida').value=''
                window.location.href = "/lista_canchas";

   
        },
        error: function(error) {
            // Manejar los errores del servidor
            console.log('Error en el envío: ', error);
            
          }
        });
    })
});

/* modal eliminar bebida*/ 
$(document).ready(function() 
{
    $('.eliminar-bebida-admin').on('click', function() 
    {
        $('#modal_eliminar_bebida_admin').modal('show')
        $('#modal_eliminar_bebida_admin').on('click', '.close, .btn-secondary',function() 
        {
             // Cerrar la modal
            $('#modal_eliminar_bebida_admin').modal('hide');  
        });
    });
});

$(document).ready(function() {
    $('.eliminar-bebida-admin').on('click', function() {
        var id_bebida = $(this).closest('tr').find('#id_bebida').val();
    console.log("id bebida: ", id_bebida)
    
       // Abrir modal de confirmación
    $('#modal_eliminar_bebida_admin').modal('show');
    
       // Manejar el click en el botón de eliminar dentro del modal
    $('#eliminar_bebida_btn').on('click', function() {
         // Envío de la solicitud de eliminación mediante AJAX
    $.ajax({
        url: '/eliminar_bebida_admin/' + id_bebida,
        type: 'DELETE',
        success: function(response) {
             // Manejar la respuesta del servidor después de eliminar el producto
            console.log(response);
            window.location.reload();
            
        },
        error: function(error) {
             // Manejar el error si ocurre algún problema durante la solicitud AJAX
            console.log(error);
        }
        
});
        
         // Cerrar el modal después de enviar la solicitud
        $('#modal_eliminar_bebida_admin').modal('hide');
    });
    });
});


/* modal administracion general*/ 

$(document).ready(function() {
    $('.modal_agregar_trabajador').on('click', function() {
        $('#modal_agregar_trabajador').modal('show');

    $('#modal_agregar_trabajador').on('click', '.close, .btn-secondary',function() {
        // Cerrar la modal
        $('#modal_agregar_trabajador').modal('hide');
})
    });
});




