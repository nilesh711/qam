function showContent(taskId){
    const contents = document.querySelectorAll('.task-content');
    contents.forEach(content=>{
        content.classList.remove('active');
    });
    const activeContent = document.getElementById(taskId);
    activeContent.classList.add('active');
}


let currentIndex =0;
const images = ['Images/image1.jpg', 'Images/image2.jpg', 'Images/image3.jpg', 'Images/image4.jpg'];

function showSlide(index){
    const carouselImage = document.getElementById('carousel-image');
    carouselImage.src = images[index];
}

function prevSlide(){
    currentIndex = (currentIndex === 0)? images.length-1 : currentIndex-1;
    showSlide(currentIndex);
}

function nextSlide(){
    currentIndex = (currentIndex === images.length-1) ? 0: currentIndex +1;
    showSlide(currentIndex);
}

document.addEventListener('DOMContentLoaded', ()=>{
    showContent('task1');
    showSlide(currentIndex);
});