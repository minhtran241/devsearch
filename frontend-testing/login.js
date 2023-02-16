var loginUrl = 'http://127.0.0.1:8000/api/users/token/';
var form = document.getElementById('login-form');
if (form)
    form.addEventListener('submit', function (e) {
        var _a, _b;
        e.preventDefault();
        var formData = {
            username: (_a = document.querySelector('input[name="username"]')) === null || _a === void 0 ? void 0 : _a.value,
            password: (_b = document.querySelector('input[name="password"]')) === null || _b === void 0 ? void 0 : _b.value
        };
        fetch(loginUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
            .then(function (res) { return res === null || res === void 0 ? void 0 : res.json(); })
            .then(function (data) {
            if (data.access) {
                localStorage.setItem('token', data.access);
                window.location =
                    'http://127.0.0.1:5500/frontend-testing/projects-list.html';
            }
            else {
                alert('username OR password did not work');
            }
        });
    });
