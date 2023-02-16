let loginBtn: HTMLElement | null = document.getElementById('login-btn');
let signoutBtn: HTMLElement | null = document.getElementById('signout-btn');

let token: string | null = localStorage.getItem('token');
if (token) loginBtn?.remove();
else signoutBtn?.remove();
signoutBtn?.addEventListener('click', (e: Event) => {
  e.preventDefault();
  localStorage.removeItem('token');
  (window as Window).location =
    'http://127.0.0.1:5500/frontend-testing/login.html';
});
const projectsUrl: string = 'http://127.0.0.1:8000/api/projects/';

let getProjects = () => {
  fetch(projectsUrl)
    .then((response) => response.json())
    .then((data) => buildProjects(data));
};

let buildProjects = (projects: any) => {
  let projectsWrapper: HTMLElement | null =
    document.getElementById('projects--wrapper');
  if (projectsWrapper) projectsWrapper.innerHTML = '';
  for (const project of projects) {
    let projectCard: string = `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.featured_image}" />
                    
                    <div>
                        <div class="card--header">
                            <h3>${project.title}</h3>
                            <strong class="vote--option" data-vote="up" data-project="${
                              project.id
                            }" >&#43;</strong>
                            <strong class="vote--option" data-vote="down" data-project="${
                              project.id
                            }"  >&#8722;</strong>
                        </div>
                        <i>${project.vote_ratio}% Positive feedback </i>
                        <p>${project.description.substring(0, 150)}</p>
                    </div>
                
                </div>
        `;
    if (projectsWrapper) projectsWrapper.innerHTML += projectCard;
  }

  addVoteEvents();
};

let addVoteEvents = () => {
  let voteButtons: HTMLCollectionOf<Element> =
    document.getElementsByClassName('vote--option');

  for (let i = 0; i < voteButtons.length; i++) {
    let token: string | null = localStorage.getItem('token');
    voteButtons[i].addEventListener('click', (e: Event) => {
      let vote: string | undefined = (e.target as HTMLElement).dataset.vote;
      let project: string | undefined = (e.target as HTMLElement).dataset
        .project;
      fetch(`${projectsUrl}${project}/vote/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ value: vote }),
      })
        .then((res) => res?.json())
        .then((data) => console.log(data));
    });
  }
};

getProjects();
