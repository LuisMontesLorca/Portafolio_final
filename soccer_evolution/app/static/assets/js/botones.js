var editButton = document.getElementById('edit-button');
var saveButton = document.getElementById('save-button');
var fields = document.querySelectorAll('input:not([type="submit"]), select');

// Función para habilitar los campos y deshabilitar los botones
function enableFields() {
  fields.forEach(function(field) {
    field.disabled = false;
  });
  editButton.disabled = true;
  saveButton.disabled = false;
}

// Función para deshabilitar los campos y habilitar el botón "Editar"
function disableFields() {
  fields.forEach(function(field) {
    field.disabled = true;
  });
  editButton.disabled = false;
  saveButton.disabled = true;
}

// Asignar eventos a los botones
editButton.addEventListener('click', enableFields);
saveButton.addEventListener('click', disableFields);