const track = document.getElementById('carouselTrack');
const items = Array.from(track.children);
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const itemCount = items.length;
let angle = 0;
const angleIncrement = 360 / itemCount;

const updateCarousel = () => {
    track.style.transform = `rotateY(${angle}deg)`;
};

nextButton.addEventListener('click', () => {
    angle -= angleIncrement;
    updateCarousel();
});

prevButton.addEventListener('click', () => {
    angle += angleIncrement;
    updateCarousel();
});

function scrollToSection(section) {
    document.querySelector(section).scrollIntoView({ behavior: 'smooth' });
}

window.addEventListener('scroll', function() {
    const scrollPosition = window.pageYOffset;
    document.querySelector('.parallax-img').style.transform = `translate(-50%, ${scrollPosition * 1}px)`;
});

document.addEventListener('DOMContentLoaded', function() {
    const videoContainers = document.querySelectorAll('.thumbnail');

    videoContainers.forEach(container => {
        container.addEventListener('click', function () {
            const videoId = container.getAttribute('data-video');
            const modal = document.getElementById('videoModal');
            const modalVideo = document.getElementById('videoFrame');

            modalVideo.src = `https://www.youtube.com/embed/${videoId}`;
            modal.classList.add('show');
            modal.style.display = 'flex';
        });
    });

    const modal = document.getElementById('videoModal');
    const modalVideo = document.getElementById('videoFrame');
    const closeBtn = document.querySelector('.modal .close');

    closeBtn.addEventListener('click', function () {
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = 'none';
            modalVideo.src = '';
        }, 300);
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
                modalVideo.src = '';
            }, 300);
        }
    });
});
