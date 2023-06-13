
$(document).ready(function() {
    $('.eliminar-btn').click(function() {
        var id_carro = $(this).data('id');
        var filaProducto = $(this).closest('tr');
        $.ajax({
            url: '/carro_compras/' + id_carro,
            type: 'DELETE',
            success: function(response) {
                // Manejar la respuesta del servidor después de eliminar el producto
                console.log(response);
                filaProducto.remove();
            },
            error: function(error) {
                // Manejar el error si ocurre algún problema durante la solicitud AJAX
                console.log(error);
            }
        });
    });
});

$(document).ready(function() {
    $('.vaciar-btn').click(function() {
    console.log("voy a vaciar el carro!!!!!!!!!!!")
        $.ajax({
            url: '/vaciar_carro_compras',
            type: 'DELETE',
            success: function(response) {
                // Manejar la respuesta del servidor después de eliminar el producto
                console.log(response);
                
            },
            error: function(error) {
                // Manejar el error si ocurre algún problema durante la solicitud AJAX
                console.log(error);
            }
        });
    });
});

$(document).ready(function() {
    // Agregar evento de clic al botón "Agregar al carro"
    $('#agregarAlCarro').click(function(event) {
    event.preventDefault(); // Evitar el envío predeterminado del formulario

    // Obtener los datos del formulario
    var nombre = $('#nombre').val();

    // Realizar la petición AJAX para enviar los datos
    $.ajax({
        url: '/agregar_al_carro',
        method: 'POST',
        data: {
        nombre: nombre
        },
        success: function(response) {
        // Mostrar la modal
        $('#modal').show();
        }
    });
    });

    // Cerrar la modal al hacer clic en el botón "Cerrar"
    $('#cerrarModal').click(function() {
    $('#modal').hide();
    });
});


//function actualizarNumeroProductos() {
// //   $.ajax({
// //     url: '/ruta_para_obtener_numero_productos',  // Reemplaza esto con la URL correcta para obtener el número de productos
// //     method: 'GET',
// //     success: function(response) {
// //       var numProductos = response.count_productos;
// //       $('#num-productos').text(numProductos);
// //     },
// //     error: function(error) {
// //       console.log('Error al obtener el número de productos:', error);
// //     }
// //   });
// // }
// // 
// // // Llama a la función para actualizar el número de productos inicialmente
 // actualizarNumeroProductos();