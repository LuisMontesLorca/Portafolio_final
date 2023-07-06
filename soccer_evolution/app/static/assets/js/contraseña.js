$(document).ready(function() {
    $('.modal_olvido').on('click', function() {
        $('#modal_olvido_contraseña').modal('show');

    $('#modal_olvido_contraseña').on('click', '.close, .btn-secondary',function() {
        // Cerrar la modal
        $('#modal_olvido_contraseña').modal('hide');
})
    });
});


$(document).ready(function() {
    $('#recuperar_btn').on('click', function() {
        console.log("click")
    
        var correo = document.getElementById('correo_recuperacion').value;
        console.log('correo_recuperacion', correo);
        if (correo !='' )
        {
            var formData = {
                correo: correo
              };
              console.log ("ESTA ES LA DATA: " + formData)
              let timerInterval
              Swal.fire({
                title: 'Enviando correo de verificación',
                html: 'Esto puede tardar unos segundos.',
                background: 'rgba(42, 47, 74, 0.975)',
    
                timer: 4200,
                timerProgressBar: true,
                didOpen: () => {
                  Swal.showLoading()
                  const b = Swal.getHtmlContainer().querySelector('b')
                  timerInterval = setInterval(() => {
                    b.textContent = Swal.getTimerLeft()
                  }, 100)
                },
                willClose: () => {
                  clearInterval(timerInterval)
                }
              }).then((result) => {
                /* Read more about handling dismissals below */
                if (result.dismiss === Swal.DismissReason.timer) {
                  console.log('I was closed by the timer')
                }
              })
              $.ajax({
                url: '/recuperar_correo',
                type: 'POST',
                contentType: 'application/json', // Configura el tipo de contenido como JSON
                data: JSON.stringify(formData),
                success: function(response){
                    if (response == 1)
                    {
                        console.log(response)
                        // Manejar la respuesta del servidor
                        console.log('Envío exitoso');
                        $('#modal_olvido_contraseña').modal('hide');
                        mostrarRecuperarContraseña()
                        document.getElementById('correo_recuperacion').value = '';
                    }
                    else
                    {
                        $('#modal_olvido_contraseña').modal('hide');
                        mostrarRecuperarContraseñaError()
                        document.getElementById('correo_recuperacion').value = '';
                    }
         
                  // Puedes realizar acciones adicionales después de enviar los datos del formulario
                },
                error: function(error) {
                  // Manejar los errores del servidor
                  console.log('Error en el envío: ', error);
                  
                }
              });
        }else{
            mostrarAlertaCorreoVacio();
        }
        
 
    });
});


$(document).ready(function() {
    $('.btn_modal_contraseña').on('click', function() {
        $('#modal_cambio_contraseña').modal('show');

    $('#modal_cambio_contraseña').on('click', '.close, .btn-secondary', function() {
        // Cerrar la modal
        $('#modal_cambio_contraseña').modal('hide');
        })
    });
});


$(document).ready(function() {
    $('#recuperar_contraseña_btn').on('click', function() {
        console.log("click")
    
        var correo_login_cambio = document.getElementById('correo_login_cambio').value;
        console.log('correo_recuperacion', correo_login_cambio);
        var contraseña_login_cambio = document.getElementById('contraseña_login_cambio').value;
        console.log('contraseña_login_cambio', contraseña_login_cambio);
        var contraseña_login_confirm = document.getElementById('contraseña_login_confirm').value;
        console.log('contraseña_login_confirm', contraseña_login_confirm);
        if (contraseña_login_cambio==contraseña_login_confirm)
        {
            var formData = {
                correo_login_cambio: correo_login_cambio,
                contraseña_login_cambio:contraseña_login_cambio,
                contraseña_login_confirm:contraseña_login_confirm
              };
   
              console.log ("ESTA ES LA DATA: " + formData)
              $.ajax({
                url: '/cambio_contraseña_ajax',
                type: 'POST',
                contentType: 'application/json', // Configura el tipo de contenido como JSON
                data: JSON.stringify(formData),
                success: function(response){
                    if (response == 1)
                    {
                        console.log(response)
                        // Manejar la respuesta del servidor
                        console.log('Envío exitoso');

                            $('#modal_contraseña_cambiada').modal('show');
                    
                            $('#modal_contraseña_cambiada').on('click', '.close, .btn-secondary', function() {
                                // Redireccionar al login
                                window.location.href = '/';
                              });
                     

                 
                    }
                    else
                    {
                        alert("no hubo cambios")
                    }
         
                  // Puedes realizar acciones adicionales después de enviar los datos del formulario
                },
                error: function(error) {
                  // Manejar los errores del servidor
                  console.log('Error en el envío: ', error);
                  
                }
              });
        }
        else
        {
            mostrarContraseñaNoCompatible()
        }

 
    });
});