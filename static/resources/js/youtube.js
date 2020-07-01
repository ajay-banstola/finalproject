const dummyYoutube = [
  {
    image: 'resources/images/dummyimage2.jpg',
    title: '1. Super ultra hot videos Super ultra hot videos Super ultra hot videos',
    view: ' 30.000',
  },
  {
    image: 'resources/images/dummyimage3.jpg',
    title: '2. Super ultra hot videos Super ultra hot videos Super ultra hot videos',
    view: ' 20.000',
  },
  {
    image: 'resources/images/dummyimage4.jpg',
    title: '3. Super ultra hot videos Super ultra hot videos Super ultra hot videos',
    view: ' 10.000',
  },
];

var listcard = document.getElementById('youtube').getElementsByClassName('card-list')[0];

for (var i = 0; i < dummyYoutube.length; i++) {
  var icon = document.createElement('I');
  var videoview = document.createElement('DIV');
  var videotitle = document.createElement('DIV');
  var content = document.createElement('DIV');
  var videoimage = document.createElement('IMG');
  var card = document.createElement('DIV');
  var cardcontainer = document.createElement('DIV');

  videoview.classList.add('video-view');
  icon.className = 'fas fa-eye';
  videoview.appendChild(icon);
  var pview = document.createTextNode(dummyYoutube[i].view);
  videoview.appendChild(pview);

  videotitle.classList.add('video-title');
  var ptitle = document.createTextNode(dummyYoutube[i].title);
  videotitle.appendChild(ptitle);

  content.classList.add('content');
  content.appendChild(videotitle);
  content.appendChild(videoview);

  videoimage.classList.add('video-image');
  videoimage.setAttribute('src', dummyYoutube[i].image);

  card.classList.add('card');
  card.classList.add('navigate');
  card.appendChild(videoimage);
  card.appendChild(content);

  cardcontainer.classList.add('card-container');
  cardcontainer.appendChild(card);

  listcard.appendChild(cardcontainer);
}
