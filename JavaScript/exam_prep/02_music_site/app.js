window.addEventListener("load", solve);

function solve() {
  let likes = 0;
  let inputFields = {
    genre: document.getElementById("genre"),
    name: document.getElementById("name"),
    author: document.getElementById("author"),
    date: document.getElementById("date"),
  };

  let addBtn = document.getElementById("add-btn");
  addBtn.setAttribute("type", "button");
  addBtn.addEventListener("click", addSong);

  let allHits = document.querySelector(".all-hits-container");
  let saveHits = document.querySelector(".saved-container");
  let totalLikes = document.querySelector("#total-likes > .likes > p");

  function saveSong(e) {
    let song = e.currentTarget.parentNode;
    song.remove();
    saveHits.appendChild(song);

    removeBtns(song);

  }

  function deleteSong(e) {
    let parent = e.currentTarget.parentNode;
    parent.remove();
  }

  function likeSong(e) {
    likes += 1;
    totalLikes.textContent = `Total Likes: ${likes}`;
    e.currentTarget.setAttribute("disabled", true);
  }

  function addSong() {
    if (!checkCorrectInput()) {
      return;
    }

    let newDiv = createElement("div", "", allHits, ["hits-info"]);

    let newImg = createElement(
      "img",
      "",
      newDiv,
      "",
      "",
      "./static/img/img.png"
    );
    let genre = createElement(
      "h2",
      `Genre: ${inputFields.genre.value}`,
      newDiv
    );
    let songName = createElement(
      "h2",
      `Name: ${inputFields.name.value}`,
      newDiv
    );
    let author = createElement(
      "h2",
      `Author: ${inputFields.author.value}`,
      newDiv
    );
    let date = createElement("h3", `Date: ${inputFields.date.value}`, newDiv);

    let saveBtn = createElement("button", "Save song", newDiv, ["save-btn"]);
    let likeBtn = createElement("button", "Like song", newDiv, ["like-btn"]);
    let deleteBtn = createElement("button", "Delete", newDiv, [
      "delete-btn",
    ]);

    likeBtn.addEventListener("click", likeSong);
    deleteBtn.addEventListener("click", deleteSong);
    saveBtn.addEventListener("click", saveSong);

    clearInputsFields();
  }

  function checkCorrectInput() {
    let values = Object.values(inputFields);
    for (const item of values) {
      if (item.value === "") {
        return false;
      }
    }

    return true;
  }

  function clearInputsFields() {
    Object.values(inputFields).forEach(element => {
      element.value = "";
    });
  }
  function removeBtns(song) {
    let saveBtn = song.querySelector(".save-btn");
    let likeBtn = song.querySelector(".like-btn");

    saveBtn.remove();
    likeBtn.remove();
  }

  function createElement(type, content, parent, classNames, id, source) {
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

    if (id) {
      htmlElement.setAttribute("id", id);
    }

    if (source && type === "img") {
      htmlElement.src = source;
    }

    return htmlElement;
  }
}
