window.addEventListener("load", solve)

function solve() {
  const publishBtn = document.getElementById("form-btn");
  const firstName = document.getElementById("first-name");
  const lastName = document.getElementById("last-name");
  const age = document.getElementById("age");
  const storyTitle = document.getElementById("story-title");
  const story = document.getElementById("story");
  const previewSection = document.getElementById("preview-list");
  const genre = document.getElementById("genre");

  publishBtn.addEventListener("click", publishStory);

  function publishStory() {
    if (checkValidInputs()) {
      return;
    }

    let newLi = createElement("li", "", previewSection, ["story-info"]);

    let newArticle = createElement("article", "", newLi);
    let nameHeader = createElement(
      "h4",
      `Name: ${firstName.value} ${lastName.value}`,
      newArticle
    );
    let ageP = createElement("p", `Age: ${age.value}`, newArticle);
    let titleP = createElement("p", `Title: ${storyTitle.value}`, newArticle);
    let genreP = createElement(
      "p",
      `Genre: ${genre.options[genre.selectedIndex].text}`,
      newArticle
    );
    let storyP = createElement("p", `${story.value}`, newArticle);

    let saveBtn = createElement("button", "Save story", newLi, ["save-btn"]);
    let editBtn = createElement("button", "Edit story", newLi, ["edit-btn"]);
    let deleteBtn = createElement("button", "Delete story", newLi, [
      "delete-btn",
    ]);

    saveBtn.addEventListener("click", saveStory);
    editBtn.addEventListener("click", editStory);
    deleteBtn.addEventListener("click", deleteStory);

    publishBtn.setAttribute("disabled", true);
    clearForm();
  }

  function saveStory() {
    let element = document.getElementById("main");
    element.textContent = "";
    let h1 = createElement("h1", "Your scary story is saved!", element);
  }

  function editStory() {
    let liInfo = Array.from(document.querySelector(".story-info").children)[0]
      .children;
    firstName.value = liInfo[0].textContent.split(": ")[1].split(" ")[0];
    lastName.value = liInfo[0].textContent.split(": ")[1].split(" ")[1];
    storyTitle.value = liInfo[2].textContent.split(": ")[1];
    age.value = liInfo[1].textContent.split(": ")[1];
    genre.value = liInfo[3].textContent.split(": ")[1];

    story.value = liInfo[4].textContent;

    publishBtn.removeAttribute("disabled");
    clearPreview();
  }

  function deleteStory() {
    clearPreview();
    publishBtn.removeAttribute("disabled");
  }

  function checkValidInputs() {
    if (
      firstName.value === "" ||
      lastName.value === "" ||
      age.value === "" ||
      storyTitle.value === "" ||
      story.value === "" ||
      genre.selectedIndex === -1
    ) {
      return true;
    }

    return false;
  }

  function clearForm() {
    firstName.value = "";
    lastName.value = "";
    age.value = "";
    storyTitle.value = "";
    story.value = "";

    genre.selectedIndex = -1;
  }

  function clearPreview() {
    let element = document.querySelector(".story-info");
    element.parentNode.removeChild(element);
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
      htmlElement.classList.add(...classNames);
    }

    return htmlElement;
  }
}
