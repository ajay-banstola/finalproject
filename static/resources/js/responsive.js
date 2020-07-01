/* Header */
const body = document.body;
const header = document.getElementById('header');

headerTogger = () => {
  header.classList.toggle('responsive');
  body.classList.toggle('disable-scrolling');
}

window.onscroll = () => {
  this.stickyHeader();
}

stickyHeader = () => {
  if (window.pageYOffset > 0) {
    header.classList.add('non-transparent-bg');
  } else {
    header.classList.remove('non-transparent-bg');
  }
}
