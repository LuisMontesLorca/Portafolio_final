// Función para cargar las provincias según la región seleccionada
function cargarProvinciasPorRegion() {
    var selectRegion = document.getElementById("region_usuario");
    var selectProvincia = document.getElementById("provincia_usuario");
  
    // Capturar el valor seleccionado en el select de regiones
    var selectedRegion = selectRegion.value;
  
    // Realizar una llamada AJAX para obtener las provincias de la región seleccionada
    $.ajax({
      url: '/obtener_provincias',
      type: 'POST',
      data: { region_id: selectedRegion },
      dataType: 'json',
      success: function(response) {
        // Limpiar el select de provincias
        selectProvincia.innerHTML = "";
  
        // Agregar la opción predeterminada
        var optionDefault = document.createElement("option");
        optionDefault.value = "";
        optionDefault.text = "Seleccione provincia";
        selectProvincia.appendChild(optionDefault);
  
        // Agregar las opciones de las provincias obtenidas
        response.forEach(function(provincia) {
          var option = document.createElement("option");
          option.value = provincia.id_provincia;
          option.text = provincia.provincia;
          selectProvincia.appendChild(option);
        });
      },
      error: function(error) {
        console.log('Error en la llamada AJAX:', error);
      }
    });
  }
  
  // Asignar el evento onchange al select de regiones en editar_usuario
  var selectRegion = document.getElementById("region_usuario");
  selectRegion.addEventListener("change", cargarProvinciasPorRegion);


  
// Función para cargar las comunas según la provincia seleccionada
function cargarComunasPorProvincia() {
    var selectProvincia = document.getElementById("provincia_usuario");
    var selectComuna = document.getElementById("comuna_usuario");
  
    // Capturar el valor seleccionado en el select de provincias
    var selectedProvincia = selectProvincia.value;
  
    // Realizar una llamada AJAX para obtener las comunas de la provincia seleccionada
    $.ajax({
      url: '/obtener_comunas',
      type: 'POST',
      data: { provincia_id: selectedProvincia },
      dataType: 'json',
      success: function(response) {
        // Limpiar el select de comunas
        selectComuna.innerHTML = "";
  
        // Agregar la opción predeterminada
        var optionDefault = document.createElement("option");
        optionDefault.value = "";
        optionDefault.text = "Seleccione comuna";
        selectComuna.appendChild(optionDefault);
  
        // Agregar las opciones de las comunas obtenidas
        response.forEach(function(comuna) {
          var option = document.createElement("option");
          option.value = comuna.id_comuna;
          option.text = comuna.comuna;
          selectComuna.appendChild(option);
        });
      },
      error: function(error) {
        console.log('Error en la llamada AJAX:', error);
      }
    });
  }
  
  // Asignar el evento onchange al select de provincias
  var selectProvincia = document.getElementById("provincia_usuario");
  selectProvincia.addEventListener("change", cargarComunasPorProvincia);
  


