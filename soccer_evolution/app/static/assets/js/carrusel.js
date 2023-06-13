var carousel = document.querySelector('.carousel');
var slides = carousel.querySelectorAll('.slide');
var currentIndex = 0;

function showSlide(index) {
  slides.forEach(function(slide, i) {
    slide.style.display = (i === index) ? 'block' : 'none';
  });
}

function nextSlide() {
  currentIndex++;
  if (currentIndex >= slides.length) {
    currentIndex = 0;
  }
  showSlide(currentIndex);
}

function prevSlide() {
  currentIndex--;
  if (currentIndex < 0) {
    currentIndex = slides.length - 1;
  }
  showSlide(currentIndex);
}

showSlide(currentIndex); // Mostrar el primer slide al cargar la página
