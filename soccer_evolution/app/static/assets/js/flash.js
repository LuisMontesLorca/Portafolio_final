// Esperar 3 segundos y luego ocultar los mensajes flash
setTimeout(function() {
    var flashContainer = document.getElementById("flash-messages-container");
    if (flashContainer) {
      flashContainer.style.display = "none";
    }
  }, 3000);