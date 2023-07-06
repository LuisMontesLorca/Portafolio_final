  
$(document).ready(function() {
  $('#btn_vaciar_carro').click(function() {
    console.log("voy a vaciar el carro!!!!!!!!!!!");
    $.ajax({
      url: '/vaciar_carro_compras',
      type: 'DELETE',
      success: function(response) {
        // Manejar la respuesta del servidor después de vaciar el carro
        console.log(response);
        window.location.href = '/';
      },
      error: function(error) {
        // Manejar el error si ocurre algún problema durante la solicitud AJAX
        console.log(error);
      }
    });
  });
});