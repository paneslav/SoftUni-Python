function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);

  function onClick() {
    // get all rows and clear them on each Search click
    let allTableRows = Array.from(document.querySelectorAll("tbody > tr"));
    allTableRows.forEach((element) => {
      element.className = "";
    });

    const inputField = document.getElementById("searchField");
    // get word from search input
    let searchedWord = inputField.value;

    // get all table boxes
    let allTableData = Array.from(document.querySelectorAll("tbody > tr > td"));

    // iterate through all the boxes to find matches
    for (const item of allTableData) {
      let parent = item.parentElement;
      let foundWord = [...item.textContent.matchAll(searchedWord)];

      //attach class select if word is found
      if (foundWord.length !== 0) {
        parent.className = "select";
      }
    }
    inputField.value = "";
  }
}
