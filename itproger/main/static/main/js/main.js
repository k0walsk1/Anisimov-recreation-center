
document.addEventListener('DOMContentLoaded', function () {
  // Your existing logic for filtering works
  document.addEventListener('click', function (e) {
    const targetElement = e.target;

    if (targetElement.classList.contains('items-works__type') && !targetElement.classList.contains('active')) {
      const activeElement = document.querySelector('.items-works__type.active');
      const elements = document.querySelectorAll('.items-works__item');
      const elementType = targetElement.dataset.workType;

      activeElement.classList.remove('active');
      targetElement.classList.add('active');

      elements.forEach(element => {
        !elementType || element.dataset.workType === elementType ? (element.style.display = 'block') : (element.style.display = 'none');
      });
    }
  });

  // Swiper initialization
  new Swiper('.mySwiper', {
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
      clickable: true,
    },
    slidesPerView: 1,
    spaceBetween: 30,
    slidesPerGroup: 1,
    centeredSlides: true,
    initialSlide: 0,
    loop: true,
    speed: 500,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
  });
  
});