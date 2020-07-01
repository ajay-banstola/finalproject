const dummyIntroduction = {
  image: [
    'resources/images/dummyimage1.jpg',
    'resources/images/dummyimage2.jpg',
    'resources/images/dummyimage3.jpg',
    'resources/images/dummyimage4.jpg',
  ],
  content:
    'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet,repudiandae excepturi ducimus animi omnis rerum? Accusantium alias repellendus minimaharum, similique ea mollitia sit omnis deleniti totam perferendis!',
  special: 'Hello World',
};

var main = document.getElementById('content-main');
main.innerHTML = dummyIntroduction.content;

var special = document.getElementsByClassName('content-special');
for (var i = 0; i < special.length; i++) {
  var text = document.createTextNode(dummyIntroduction.special);
  special[i].appendChild(text);
}

var imageshow = document.getElementsByClassName('image-show');
for (var i = 0; i < imageshow.length; i++) {
  imageshow[i].setAttribute(
    'style',
    `background-image: url(${dummyIntroduction.image[i]}); background-size: 100% 100%`,
  );
}

var sliderdot = document.getElementsByClassName('dot');
var imageindex = 0;
backImage = () => {
  imageshow[imageindex].style.display = 'none';
  sliderdot[imageindex].classList.remove('dot-active');
  if (imageindex == 0) {
    imageindex = imageshow.length;
  }
  imageshow[imageindex - 1].style.display = 'block';
  sliderdot[imageindex - 1].classList.add('dot-active');
  imageindex--;
};

forwardImage = () => {
  imageshow[imageindex].style.display = 'none';
  sliderdot[imageindex].classList.remove('dot-active');
  imageindex++;
  if (imageindex == imageshow.length) {
    imageindex = 0;
  }
  imageshow[imageindex].style.display = 'block';
  sliderdot[imageindex].classList.add('dot-active');
};
