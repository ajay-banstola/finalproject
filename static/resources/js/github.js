const dummyGithub = [
  {
    title: 'Lorem ipsum',
    description:
      'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet, repudiandae excepturi ducimus animi omnis rerum?',
  },
  {
    title: 'Lorem ipsum',
    description:
      'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet, repudiandae excepturi ducimus animi omnis rerum?',
  },
  {
    title: 'Lorem ipsum',
    description:
      'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime voluptatibus eveniet, repudiandae excepturi ducimus animi omnis rerum?',
  },
];

var cardlist = document.getElementById('github').getElementsByClassName('card-list')[0];

for (var i = 0; i < dummyGithub.length; i++) {
  var title = document.createElement('DIV');
  title.classList.add('git-title');
  title.appendChild(document.createTextNode(dummyGithub[i].title));

  var descrp = document.createElement('DIV');
  descrp.classList.add('git-descrp');
  descrp.appendChild(document.createTextNode(dummyGithub[i].description));

  var gcard = document.createElement('DIV');
  gcard.classList.add('card');
  gcard.classList.add('navigate');
  gcard.appendChild(title);
  gcard.appendChild(descrp);

  var container = document.createElement('DIV');
  container.classList.add('card-container');
  container.appendChild(gcard);

  cardlist.appendChild(container);
}
