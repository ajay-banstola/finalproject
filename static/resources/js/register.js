const regSubmit = document.getElementById('reg-btn');
let username;

function register() {
    const userData = {
        fullName: document.getElementById('reg-name').value,
        email: document.getElementById('reg-email').value,
        password: document.getElementById('reg-password').value
    };
    axios.post(registerURL, userData)
    .then(response => {
        showSuccessMessage();
    })
    .catch(error => {
        console.log(error);
    });
    
    username = userData.fullName;
}

function showSuccessMessage() {
    const form = document.getElementById('form-container');
    form.style.display = 'none';
    const btn = document.getElementById('log-in');
    btn.style.display = 'none';
    
    const welcome = document.createElement('div');
    welcome.id = 'welcome-text';
    const popup = document.getElementById('success-popup');
    popup.appendChild(welcome);
    welcome.appendChild(document.createTextNode('Welcome ' + username));
    popup.classList.toggle('d-none');
}

regSubmit.addEventListener('click', register);