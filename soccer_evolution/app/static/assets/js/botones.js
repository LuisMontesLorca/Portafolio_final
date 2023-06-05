
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
