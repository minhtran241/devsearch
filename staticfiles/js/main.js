// GET SEARCH FORM AND PAGE LINKS (PAGINATION BUTTONS)
let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');

// ENSURE SEARCH FORM EXISTS
if (searchForm) {
  for (const pageLink of pageLinks) {
    pageLink.addEventListener('click', function (e) {
      e.preventDefault();
      // GET THE DATA ATTRIBUTE
      let page = this.dataset.page;

      // ADD HIDDEN SEARCH INPUT TO FORM
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`;

      // SUBMIT FORM
      searchForm.submit();
    });
  }
}

// REMOVE TAGS WHEN UPDATE PROJECT (PROJECT FORM)
let tags = document.getElementsByClassName('project-tag');

for (const tag of tags) {
  tag.addEventListener('click', (e) => {
    let tagId = e.target.dataset.tag;
    let projectId = e.target.dataset.project;
    fetch('http://127.0.0.1:8000/api/remove-tag/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ project: projectId, tag: tagId }),
    })
      .then((res) => res.json())
      .then((data) => {
        e.target.remove();
      });
  });
}
