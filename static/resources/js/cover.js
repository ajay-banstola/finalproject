const dummyCover = 'https://healthitanalytics.com/images/site/features/ThinkstockPhotos-518311330.jpg';

const str = 'Why Use Lead Predict?';

let coverBackground = document.getElementById('cover'); 
let titleContainer = document.getElementsByClassName('cover-title');
let coverTitle = document.createElement('H1');
titleContainer[0].appendChild(coverTitle);

coverBackground.setAttribute('style',
`background-image: url(${dummyCover})`,
);

add = (i) => {
  if(i >= str.length) return;
	coverTitle.innerHTML += str[i];
  setTimeout(add, 180, i+1);
}

add(0);

