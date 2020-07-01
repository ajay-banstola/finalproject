const dummyBlog = [
  {
    image: 'resources/images/dummyimage2.jpg',
    title: '1. Super ultra hot posts',
    content:
      'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet,repudiandae excepturi ducimus animi omnis rerum? Accusantium alias repellendus minimaharum, similique ea mollitia sit omnis deleniti totam perferendis!',
    view: ' 30.000',
  },
  {
    image: 'resources/images/dummyimage3.jpg',
    title: '2. Super ultra hot posts',
    content:
      'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet,repudiandae excepturi ducimus animi omnis rerum? Accusantium alias repellendus minimaharum, similique ea mollitia sit omnis deleniti totam perferendis!',
    view: ' 20.000',
  },
  {
    image: 'resources/images/dummyimage4.jpg',
    title: '3. Super ultra hot posts',
    content:
      'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet,repudiandae excepturi ducimus animi omnis rerum? Accusantium alias repellendus minimaharum, similique ea mollitia sit omnis deleniti totam perferendis!',
    view: ' 10.000',
  },
];

var listcard = document.getElementById('blog').getElementsByClassName('card-list')[0];

for (var i = 0; i < dummyBlog.length; i++) {
  var icon = document.createElement('I');
  var postview = document.createElement('DIV');
  var postcontent = document.createElement('DIV');
  var posttitle = document.createElement('DIV');
  var content = document.createElement('DIV');
  var postimage = document.createElement('IMG');
  var card = document.createElement('DIV');
  var cardcontainer = document.createElement('DIV');

  postview.classList.add('post-view');
  icon.className = 'fas fa-eye';
  postview.appendChild(icon);
  var pview = document.createTextNode(dummyBlog[i].view);
  postview.appendChild(pview);

  postcontent.classList.add('post-content');
  var pcontent = document.createTextNode(dummyBlog[i].content);
  postcontent.appendChild(pcontent);

  posttitle.classList.add('post-title');
  var ptitle = document.createTextNode(dummyBlog[i].title);
  posttitle.appendChild(ptitle);

  content.classList.add('content');
  content.appendChild(posttitle);
  content.appendChild(postcontent);
  content.appendChild(postview);

  postimage.classList.add('post-image');
  postimage.setAttribute('src', dummyBlog[i].image);

  card.classList.add('card');
  card.classList.add('navigate');
  card.appendChild(postimage);
  card.appendChild(content);

  cardcontainer.classList.add('card-container');
  cardcontainer.appendChild(card);

  listcard.appendChild(cardcontainer);
}
