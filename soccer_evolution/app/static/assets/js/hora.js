$(document).ready(function() {
    $('#hora_inicio').on('change', function() {
      var horaInicio = $(this).val();
      $('#hora_fin option').each(function() {
        if ($(this).val() <= horaInicio) {
          $(this).hide();
        } else {
          $(this).show();
        }
      });
    });
  });