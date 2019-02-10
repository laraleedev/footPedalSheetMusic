const images = document.getElementById('images');

let currentChildren;
let totalImages;

images.ondragover = () => {
    return false;
};

images.ondragleave = () => {
    return false;
};

images.ondragend = () => {
    return false;
};

images.ondrop = (e) => {
    e.preventDefault();

    while (images.firstChild) { // Clear all current images first
        images.removeChild(images.firstChild);
    }

    let files = [...e.dataTransfer.files].map(file => file.path).sort();

    totalImages = files.length;

    for (let f of files) {
        let newImage = document.createElement('img');

        newImage.setAttribute('class', 'music-image');
        newImage.setAttribute('src', f);
        images.appendChild(newImage);
    }

    currentChildren = images.children;
    
    return false;
};

document.addEventListener('keydown', logKey);

function logKey(e) {
  if (e.code === 'KeyN') {
    for (let x = 0; x < totalImages; x++) {
        if (isElementRightAndNotInViewport(currentChildren[x])) {
            window.scrollTo({
                top: 0,
                left: window.scrollX + currentChildren[x].getBoundingClientRect().left,
                behavior: 'smooth'
            });

            break;
        }
    }
  }
}

function isElementRightAndNotInViewport (el) {
    var rect = el.getBoundingClientRect();

    return rect.left > 0 && rect.right > (window.innerWidth || document.documentElement.clientWidth);
}