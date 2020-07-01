var dummyContributor = [
  {
    name: "dummyName",
    job: "Front end",
    city: "dummyCity",
    avatar: 'resources/images/dummyimage1.jpg'
  },
  {
    name: "dummyName2",
    job: "Back end",
    city: "dummyCity",
    avatar: 'resources/images/dummyimage2.jpg'
  },
  {
    name: "dummyName3",
    job: "Devops",
    city: "dummyCity",
    avatar: 'resources/images/dummyimage3.jpg'
  },
  {
    name: "dummyName4",
    job: "Full stack",
    city: "dummyCity",
    avatar: 'resources/images/dummyimage4.jpg'
  },
  {
    name: "dummyName5",
    job: "Devops",
    city: "dummyCity",
    avatar: 'resources/images/dummyimage1.jpg'
  },
];

var listDev = document.getElementsByClassName('people');

for (var i=0; i<dummyContributor.length; i++) {
  var avatar = document.createElement('IMG');
  avatar.setAttribute('src', dummyContributor[i].avatar);

  var names = document.createElement('h2');
  names.innerHTML = dummyContributor[i].name; 

  var job = document.createElement('DIV');
  job.classList.add('job');
  job.appendChild(document.createTextNode(dummyContributor[i].job));

  var city = document.createElement('DIV');
  city.appendChild(document.createTextNode(dummyContributor[i].city));

  var info = document.createElement('DIV');
  info.classList.add('info');
  info.appendChild(names);
  info.appendChild(job);
  info.appendChild(city);

  var dev = document.createElement('DIV');
  dev.classList.add('person');
  dev.appendChild(avatar);
  dev.appendChild(info);

  if (dummyContributor[i].job =='Devops') {
    listDev[1].appendChild(dev);
  }
  else {
    listDev[0].appendChild(dev);
  }
}