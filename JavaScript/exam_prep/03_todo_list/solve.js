function attachEvents() {
  const TASKS_URL = "http://localhost:3030/jsonstore/tasks/";
  const loadAllBtn = document.getElementById("load-button");
  const addBtn = document.getElementById("add-button");
  const titleField = document.getElementById("title");
  const toDoUl = document.getElementById("todo-list");

  loadAllBtn.addEventListener("click", loadAll);
  addBtn.addEventListener("click", addTask);

  async function editTask(e) {
    if (e.currentTarget.textContent === "Submit") {
      await fetch(`${TASKS_URL}${e.currentTarget.id}`, {
        method: "PATCH",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({
          name: `${e.currentTarget.parentNode.firstChild.value}`,
        }),
      });
      loadItems();
      return;
    }
    let parent = e.currentTarget.parentNode;
    let taskName = parent.firstChild.textContent;
    let inputField = createElement("input", `${taskName}`);
    inputField.setAttribute("type", "text");

    parent.removeChild(parent.firstChild);
    parent.insertBefore(inputField, parent.firstChild);

    e.currentTarget.textContent = "Submit";
  }

  async function addTask(e) {
    e.preventDefault();
    if (titleField.value === "") {
      return;
    }
    await fetch(TASKS_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: `${titleField.value}` }),
    });
    await loadItems();
    titleField.value = "";
  }

  async function loadAll(e) {
    e.preventDefault();
    await loadItems();
  }

  async function removeTask(e) {
    let parent = e.currentTarget.parentNode;
    await fetch(`${TASKS_URL}${e.currentTarget.id}`, {
      method: "DELETE",
    });
    parent.remove();
  }

  async function loadItems() {
    toDoUl.innerHTML = "";

    let request = await fetch(TASKS_URL);
    let tasks = await request.json();

    Object.values(tasks).forEach((element) => {
      let newLi = createElement("li", "", toDoUl);
      let taskName = createElement("span", element.name, newLi);
      let removeBtn = createElement("button", "Remove", newLi, "", element._id);
      let editBtn = createElement("button", "Edit", newLi, "", element._id);

      removeBtn.addEventListener("click", removeTask);
      editBtn.addEventListener("click", editTask);
    });
  }

  function createElement(type, content, parent, classNames, id) {
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

    return htmlElement;
  }
}
attachEvents();
