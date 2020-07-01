const loginForm = document.getElementById('log-in-form');
const registerForm = document.getElementById('register-form');

function togglePopup(popupId) {
  const popup = document.getElementById(popupId);
  popup.classList.toggle('d-none');
  body.classList.toggle('disable-scrolling');
}

function changeForm() {
  loginForm.classList.toggle('d-none');
  registerForm.classList.toggle('d-none');
}
