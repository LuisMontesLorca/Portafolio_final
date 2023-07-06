$(document).ready(function() {
    $('#btn_vaciar_carro').on('click', function() {
      // Abrir la modal
      $('#modal_vaciar_carro').modal('show');
    });
  
    // Manejar el evento de confirmación
    $('#confirmar-btn').on('click', function() {
      // Cerrar la modal
      $('#modal_vaciar_carro').modal('hide');
    });
  
    // Enviar el formulario mediante AJAX al hacer clic en el botón "Confirmar"
    $('#btn_confirmar_vaciar').click(function() {
      console.log("voy a vaciar el carro!!!!!!!!!!!");
      $.ajax({
        url: '/vaciar_carro_compras',
        type: 'DELETE',
        success: function(response) {
          // Manejar la respuesta del servidor después de vaciar el carro
          console.log(response);
          window.location.reload()
        },
        error: function(error) {
          // Manejar el error si ocurre algún problema durante la solicitud AJAX
          console.log(error);
        }
      });
    });
  
    // Manejar el evento de cerrar modal al hacer clic en el botón "Cerrar" o "Cancelar"
    $('#modal_vaciar_carro').on('click', '.close, .btn-secondary', function() {
      // Cerrar la modal
      $('#modal_vaciar_carro').modal('hide');
    });
  });
