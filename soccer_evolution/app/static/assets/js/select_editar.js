function cargarProvinciasPorRegion_editar() {
    var selectRegion_editar = document.getElementById("region_usuario_editar");
    console.log(selectRegion_editar)
    var selectProvincia_editar = document.getElementById("provincia_usuario_editar");
  
    // Capturar el valor seleccionado en el select de regiones
    var selectedRegion = selectRegion_editar.value;
  
    // Realizar una llamada AJAX para obtener las provincias de la región seleccionada
    $.ajax({
      url: '/obtener_provincias',
      type: 'POST',
      data: { region_id: selectedRegion },
      dataType: 'json',
      success: function(response) {
        // Limpiar el select de provincias
        selectProvincia_editar.innerHTML = "";
  
        // Agregar la opción predeterminada
        var optionDefault = document.createElement("option");
        optionDefault.value = "";
        optionDefault.text = "Seleccione provincia";
        selectProvincia_editar.appendChild(optionDefault);
  
        // Agregar las opciones de las provincias obtenidas
        response.forEach(function(provincia) {
          var option = document.createElement("option");
          option.value = provincia.id_provincia;
          option.text = provincia.provincia;
          selectProvincia_editar.appendChild(option);
        });
      },
      error: function(error) {
        console.log('Error en la llamada AJAX:', error);
      }
    });
  }
  
  // Asignar el evento onchange al select de regiones
  var selectRegion_editar = document.getElementById("region_usuario_editar");
  selectRegion_editar.addEventListener("change", cargarProvinciasPorRegion_editar);


  
  function cargarComunasPorProvincia_editar() {
    var selectProvincia_editar = document.getElementById("provincia_usuario_editar");
    var selectComuna_editar = document.getElementById("comuna_usuario_editar");
  
    // Capturar el valor seleccionado en el select de provincias
    var selectedProvincia = selectProvincia_editar.value;
  
    // Realizar una llamada AJAX para obtener las comunas de la provincia seleccionada
    $.ajax({
      url: '/obtener_comunas',
      type: 'POST',
      data: { provincia_id: selectedProvincia },
      dataType: 'json',
      success: function(response) {
        // Limpiar el select de comunas
        selectComuna_editar.innerHTML = "";
  
        // Agregar la opción predeterminada
        var optionDefault = document.createElement("option");
        optionDefault.value = "";
        optionDefault.text = "Seleccione comuna";
        selectComuna_editar.appendChild(optionDefault);
  
        // Agregar las opciones de las comunas obtenidas
        response.forEach(function(comuna) {
          var option = document.createElement("option");
          option.value = comuna.id_comuna;
          console.log (option.value)
          option.text = comuna.comuna;
          console.log (option.text)
          selectComuna_editar.appendChild(option);
        });
      },
      error: function(error) {
        console.log('Error en la llamada AJAX:', error);
      }
    });
  }
  
  // Asignar el evento onchange al select de provincias
  var selectProvincia_editar = document.getElementById("provincia_usuario_editar");
  selectProvincia_editar.addEventListener("change", cargarComunasPorProvincia_editar);
  