const loginUrl = 'http://127.0.0.1:8000/api/users/token/';
let form: HTMLElement | null = document.getElementById('login-form');
if (form)
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    let formData = {
      username: document.querySelector<HTMLInputElement>(
        'input[name="username"]'
      )?.value,
      password: document.querySelector<HTMLInputElement>(
        'input[name="password"]'
      )?.value,
    };
    fetch(loginUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((res) => res?.json())
      .then((data) => {
        if (data.access) {
          localStorage.setItem('token', data.access);
          (window as Window).location =
            'http://127.0.0.1:5500/frontend-testing/projects-list.html';
        } else {
          alert('username OR password did not work');
        }
      });
  });
