var loginBtn = document.getElementById('login-btn');
var signoutBtn = document.getElementById('signout-btn');
var token = localStorage.getItem('token');
if (token)
    loginBtn === null || loginBtn === void 0 ? void 0 : loginBtn.remove();
else
    signoutBtn === null || signoutBtn === void 0 ? void 0 : signoutBtn.remove();
signoutBtn === null || signoutBtn === void 0 ? void 0 : signoutBtn.addEventListener('click', function (e) {
    e.preventDefault();
    localStorage.removeItem('token');
    window.location =
        'http://127.0.0.1:5500/frontend-testing/login.html';
});
var projectsUrl = 'http://127.0.0.1:8000/api/projects/';
var getProjects = function () {
    fetch(projectsUrl)
        .then(function (response) { return response.json(); })
        .then(function (data) { return buildProjects(data); });
};
var buildProjects = function (projects) {
    var projectsWrapper = document.getElementById('projects--wrapper');
    if (projectsWrapper)
        projectsWrapper.innerHTML = '';
    for (var _i = 0, projects_1 = projects; _i < projects_1.length; _i++) {
        var project = projects_1[_i];
        var projectCard = "\n                <div class=\"project--card\">\n                    <img src=\"http://127.0.0.1:8000".concat(project.featured_image, "\" />\n                    \n                    <div>\n                        <div class=\"card--header\">\n                            <h3>").concat(project.title, "</h3>\n                            <strong class=\"vote--option\" data-vote=\"up\" data-project=\"").concat(project.id, "\" >&#43;</strong>\n                            <strong class=\"vote--option\" data-vote=\"down\" data-project=\"").concat(project.id, "\"  >&#8722;</strong>\n                        </div>\n                        <i>").concat(project.vote_ratio, "% Positive feedback </i>\n                        <p>").concat(project.description.substring(0, 150), "</p>\n                    </div>\n                \n                </div>\n        ");
        if (projectsWrapper)
            projectsWrapper.innerHTML += projectCard;
    }
    addVoteEvents();
};
var addVoteEvents = function () {
    var voteButtons = document.getElementsByClassName('vote--option');
    var _loop_1 = function (i) {
        var token_1 = localStorage.getItem('token');
        voteButtons[i].addEventListener('click', function (e) {
            var vote = e.target.dataset.vote;
            var project = e.target.dataset
                .project;
            fetch("".concat(projectsUrl).concat(project, "/vote/"), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: "Bearer ".concat(token_1)
                },
                body: JSON.stringify({ value: vote })
            })
                .then(function (res) { return res === null || res === void 0 ? void 0 : res.json(); })
                .then(function (data) { return console.log(data); });
        });
    };
    for (var i = 0; i < voteButtons.length; i++) {
        _loop_1(i);
    }
};
getProjects();
