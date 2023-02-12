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