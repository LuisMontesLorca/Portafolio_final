function mostrarAlertaArrendar() {
    var miAlerta = document.getElementById("alerta_arrendar");
    miAlerta.showModal();
  }
  
  function cerrarAlertaArrendar() {
    var miAlerta = document.getElementById("alerta_arrendar");
    window.location.reload()
    miAlerta.close();
  }

  function mostrarAlertaRegistro() {
    var miAlerta = document.getElementById("alert_registro");
    miAlerta.showModal();
  }
  
  function cerrarAlertaRegistro() {
    var miAlerta = document.getElementById("alert_registro");
    miAlerta.close();
  }


  function mostrarAlertaBienvenido() {
    var miAlerta = document.getElementById("alert_bienvenido");
    miAlerta.showModal();
  }
  
  function cerrarAlertaRegistro() {
    var miAlerta = document.getElementById("alert_bienvenido");
    miAlerta.close();
  }

  function mostrarRecuperarContraseña() {
    var miAlerta = document.getElementById("alerta_recuperacion_password");
    miAlerta.showModal();
  }
  
  function cerrarRecuperarContraseña() {
    var miAlerta = document.getElementById("alerta_recuperacion_password");
    miAlerta.close();
  }

  function mostrarRecuperarContraseñaError() {
    var miAlerta = document.getElementById("alerta_recuperacion_password_error");
    miAlerta.showModal();
  }
  
  function cerrarRecuperarContraseñaError() {
    var miAlerta = document.getElementById("alerta_recuperacion_password_error");
    miAlerta.close();
  }

  function mostrarContraseñaNoCompatible() {
    var miAlerta = document.getElementById("alerta_contraseña_no_compatible");
    miAlerta.showModal();
  }
  
  function cerrarContraseñaNoCompatible() {
    var miAlerta = document.getElementById("alerta_contraseña_no_compatible");
    miAlerta.close();
  }

  function mostrarAlertaBalones() {
    var miAlerta = document.getElementById("alerta_balones");
    miAlerta.showModal();
  }
  
  function cerrarAlertaBalones() {
    var miAlerta = document.getElementById("alerta_balones");
    window.location.reload()
    miAlerta.close();
  }
  function mostrarAlertaBebidas() {
    var miAlerta = document.getElementById("alerta_bebidas");
    miAlerta.showModal();
  }
  
  function cerrarAlertaBebidas() {
    var miAlerta = document.getElementById("alerta_bebidas");
    window.location.reload()
    miAlerta.close();
  }

  function mostrarAlertaCamisetas() {
    var miAlerta = document.getElementById("alerta_camisetas");
    miAlerta.showModal();
  }
  
  function cerrarAlertaCamisetas() {
    var miAlerta = document.getElementById("alerta_camisetas");
    window.location.reload()
    miAlerta.close();
  }

  function mostrarAlertaProductoEliminado() {
    var alerta = document.getElementById('alerta_producto_eliminado');
    
    // Verificar si el diálogo está cerrado antes de abrirlo
    if (!alerta.hasAttribute('open')) {
      alerta.showModal();
  
      setTimeout(function() {
        alerta.close();
      }, 4000); // 3000 milisegundos = 3 segundos
    }
  }

  
  function cerrarAlertaProductoEliminado() {
    var miAlerta = document.getElementById("alerta_producto_eliminado");
    miAlerta.close();
  }

  function mostrarAlertaCorreoVacio() {
    var miAlerta = document.getElementById("alerta_correo_vacio");
    miAlerta.showModal();
  }
  
  function cerrarAlertaCorreoVacio() {
    var miAlerta = document.getElementById("alerta_correo_vacio");
    miAlerta.close();
  }
  