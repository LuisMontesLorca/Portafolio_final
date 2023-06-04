/*var editButton = document.getElementById('edit-button');
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
*/

const openModalButton = document.getElementById('open_modal');
const closeModalButton = document.getElementById('close_modal');
const modal = document.getElementById('modal');

openModalButton.addEventListener('click', () => {
  modal.classList.add('show');
});

closeModalButton.addEventListener('click', () => {
  modal.classList.remove('show');
});

document.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.classList.remove('show');
  }
});
