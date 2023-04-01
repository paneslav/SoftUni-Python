function attachEvents() {
  const BOOKS_URL = "http://localhost:3030/jsonstore/collections/books";
  const loadBooksBtn = document.getElementById("loadBooks");
  const tbody = Array.from(document.getElementsByTagName("tbody"))[0];
  const submitBtn = Array.from(document.querySelectorAll("div > button"))[0];
  const inputFields = Array.from(document.querySelectorAll("div > input"));
  const h3 = Array.from(document.getElementsByTagName("h3"))[0];

  let bookToEdit = "";

  loadBooksBtn.addEventListener("click", loadBooks);
  submitBtn.addEventListener("click", createBook);

  function checkCorrectInput() {
    if (!inputFields[0].value || !inputFields[1].value) {
      return false;
    }

    return true;
  }
  async function editBtnHandler(key, title, author) {
    submitBtn.textContent = "Save";
    h3.textContent = "Edit FORM";

    bookToEdit = key;
    inputFields[0].value = title;
    inputFields[1].value = author;
  }

  async function deleteBook(key) {
    await fetch(`${BOOKS_URL}/${key}`, {
      method: "DELETE",
    });

    await loadBooks();
  }

  async function loadBooks() {
    let result = await fetch(BOOKS_URL);
    result = await result.json();

    tbody.innerHTML = "";
    for (const key in result) {
      let newRow = createElement("tr", "", tbody);
      let newtd = createElement("td", result[key].title, newRow);
      newtd = createElement("td", result[key].author, newRow);
      newtd = createElement("td", "", newRow);
      let editBtn = createElement("button", "Edit", newtd);
      editBtn.addEventListener("click", () =>
        editBtnHandler(key, result[key].title, result[key].author)
      );
      let dltBtn = createElement("button", "Delete", newtd);
      dltBtn.addEventListener("click", () => deleteBook(key));
    }
  }

  async function createBook() {
    if (!checkCorrectInput()) {
      return;
    }

    if (submitBtn.textContent === "Submit") {
      let book = {
        author: inputFields[1].value,
        title: inputFields[0].value,
      };

      let settings = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
      };

      await fetch(BOOKS_URL, settings);

      await loadBooks();
    } else {
      let book = {
        author: inputFields[1].value,
        title: inputFields[0].value,
      };

      let settings = {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
      };

      await fetch(`${BOOKS_URL}/${bookToEdit}`, settings);

      await loadBooks();

      h3.textContent = "FORM";
      submitBtn.textContent = "Submit";
    }

    inputFields[0].value = "";
    inputFields[1].value = "";
  }

  function createElement(type, content, parent, classNames) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (parent) {
      parent.appendChild(htmlElement);
    }

    if (classNames) {
      htmlElement.classList.add(...classNames.split(" "));
    }

    return htmlElement;
  }
}

attachEvents();
