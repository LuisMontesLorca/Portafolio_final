
$(document).ready(function() {
    $('#form_registro').validate({
      rules: {
        rut_usuario: {
          required: true
        },
        nombre_usuario: {
          required: true
        },
        apellido_usuario: {
          required: true
        },
        correo_usuario: {
          required: true
        },
        password_usuario: {
          required: true,
          minlength: 6
        },
        telefono_usuario: {
          required: true,
          number: true,
          minlength: 9,
          maxlength: 9
          
        },
        direccion_usuario: {
          required: true
        }
      },
      messages: {
        rut_usuario: {
          required:  "Por favor, ingresa tu RUT"
        },
        nombre_usuario: {
          required:  "Por favor, ingresa tu nombre"
        },
        apellido_usuario: {
          required:  "Por favor, ingresa tu apellido"
        },
        correo_usuario: {
          required:  "Por favor, ingresa tu correo"
        },
        password_usuario: {
          required:  "Por favor, ingresa tu contraseña",
          minlength: "Debe tener un mínimo de 6 caracteres"
        },
        telefono_usuario: {
          required:  "Por favor, ingresa tu telefono",
          minlength: "Debe contener 9 dígitos",
          maxlenght: "Debe contener 9 dígitos",
          number: "Deben ser solo números"
        },
        direccion_usuario: {
          required:  "Por favor, ingresa tu direccion"
        }
      },
      submitHandler: function(form) 
      {
        // Verificar si los campos requeridos están llenos antes de enviar el formulario
        if ($('#rut_usuario').val() && $('#nombre_usuario').val() && $('#apellido_usuario').val() && $('#correo_usuario').val() && $('#password_usuario').val() && $('#telefono_usuario').val() && $('#direccion_usuario').val()) {
          // Si todos los campos requeridos están llenos, enviar el formulario
          form.submit();
        }else{
          // Si falta algún campo requerido, mostrar un mensaje de error o realizar alguna otra acción
          alert('Por favor, completa todos los campos requeridos');
        }
      }
    });
  });
  


  $(document).ready(function() {
    $('#form_login').validate({
      rules: {
        correo_login: {
          required: true
        },
        contraseña_login: {
          required: true
        }

      },
      messages: {
        correo_login: {
          required:  "Por favor, ingresa tu correo"
        },
        contraseña_login: {
          required:  "Por favor, ingresa tu contraseña"
        }

      },
      submitHandler: function(form) {
        // Verificar si los campos requeridos están llenos antes de enviar el formulario
        if ($('#correo_login').val() && $('#contraseña_login').val()) {
          // Si todos los campos requeridos están llenos, enviar el formulario
          form.submit();
        } else {
          // Si falta algún campo requerido, mostrar un mensaje de error o realizar alguna otra acción
          alert('Por favor, completa todos los campos requeridos');
        }
      }
    });
  });



  $(document).ready(function() {
    $('#form_editar').validate({
      rules: {
        rut_usuario: {
          required: true
        },
        nombre_usuario: {
          required: true
        },
        apellido_usuario: {
          required: true
        },
        correo_usuario: {
          required: true
        },
        password_usuario: {
          required: true
        },
        telefono_usuario: {
          required: true,
          number: true,
          minlength: 9,
          maxlenght: 9
          
        },
        direccion_usuario: {
          required: true
        }
      },
      messages: {
        rut_usuario: {
          required:  "Por favor, ingresa tu RUT"
        },
        nombre_usuario: {
          required:  "Por favor, ingresa tu nombre"
        },
        apellido_usuario: {
          required:  "Por favor, ingresa tu apellido"
        },
        correo_usuario: {
          required:  "Por favor, ingresa tu correo"
        },
        password_usuario: {
          required:  "Por favor, ingresa tu contraseña"
        },
        telefono_usuario: {
          required:  "Por favor, ingresa tu telefono",
          minlength: "Debe contener 9 dígitos",
          maxlenght: "Debe contener 9 dígitos",
          number: "Deben ser solo números"
        },
        direccion_usuario: {
          required:  "Por favor, ingresa tu direccion"
        }
      },
      submitHandler: function(form) {
        // Verificar si los campos requeridos están llenos antes de enviar el formulario
        if ($('#rut_usuario').val() && $('#nombre_usuario').val() && $('#apellido_usuario').val() && $('#correo_usuario').val() && $('#password_usuario').val() && $('#telefono_usuario').val() && $('#direccion_usuario').val()) {
          // Si todos los campos requeridos están llenos, enviar el formulario
          form.submit();
        } else {
          // Si falta algún campo requerido, mostrar un mensaje de error o realizar alguna otra acción
          alert('Por favor, completa todos los campos requeridos');
        }
      }
    });
  });

