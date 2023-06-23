
$(document).ready(function() {
    $('.suspender-arriendo').click(function() {
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
