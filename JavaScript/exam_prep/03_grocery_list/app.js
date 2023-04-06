const GROCERY_URL = "http://localhost:3030/jsonstore/grocery/";

const tbody = document.getElementById("tbody");

const loadBtn = document.getElementById("load-product");
const addBtn = document.getElementById("add-product");
const updateBtn = document.getElementById("update-product");

loadBtn.addEventListener("click", loadItems);
addBtn.addEventListener("click", addItem);
updateBtn.addEventListener("click", updateItem);

const inputFields = {
  name: document.getElementById("product"),
  count: document.getElementById("count"),
  price: document.getElementById("price"),
};

let itemToUpdate = "";


async function deleteItem(e) {
  let itemId = e.currentTarget.id;

  await fetch(`${GROCERY_URL}${itemId}`, {
    method: "DELETE",
  });

  await loadItems();
}

async function updateItem(e) {

  if (!checkCorrectInputs()) {
    return;
  }

  await fetch(`${GROCERY_URL}${itemToUpdate}`, {
    method: "PATCH",
    body: JSON.stringify({
      product: inputFields.name.value,
      count: inputFields.count.value,
      price: inputFields.price.value,
    })
  })

  clearInputs();
  
  addBtn.removeAttribute("disabled");
  updateBtn.setAttribute("disabled", true);
  await loadItems();
}

function updateBtnHandler(e) {
  let currentItem = e.currentTarget.parentNode.parentNode;
  updateBtn.removeAttribute("disabled");
  addBtn.setAttribute("disabled", true);

  let itemName = currentItem.getElementsByClassName("name")[0];
  let itemCount = currentItem.getElementsByClassName("count-product")[0];
  let itemPrice = currentItem.getElementsByClassName("product-price")[0];

  inputFields.name.value = itemName.textContent;
  inputFields.count.value = itemCount.textContent;
  inputFields.price.value = itemPrice.textContent;

  itemToUpdate = e.currentTarget.id;
}

async function addItem(e) {
  if (e) {
    e.preventDefault();
  }

  if (!checkCorrectInputs()) {
    return;
  }

  await fetch(GROCERY_URL, {
    method: "POST",
    body: JSON.stringify({
      product: inputFields.name.value,
      count: inputFields.count.value,
      price: inputFields.price.value,
    }),
  });

  clearInputs();
  await loadItems();
}

async function loadItems(e) {
  if (e) {
    e.preventDefault();
  }
  tbody.textContent = "";
  let request = await fetch(GROCERY_URL);
  let products = await request.json();

  Object.values(products).forEach((element) => {
    let tableRow = createElement("tr", "", tbody);
    let name = createElement("td", `${element.product}`, tableRow, ["name"]);
    let count = createElement("td", `${element.count}`, tableRow, [
      "count-product",
    ]);
    let price = createElement("td", `${element.price}`, tableRow, [
      "product-price",
    ]);
    let buttons = createElement("td", "", tableRow, ["btn"]);
    let updateBtn = createElement(
      "button",
      "Update",
      buttons,
      ["update"],
      `${element._id}`
    );
    let deleteBtn = createElement(
      "button",
      "Delete",
      buttons,
      ["delete"],
      `${element._id}`
    );

    deleteBtn.addEventListener("click", deleteItem);
    updateBtn.addEventListener("click", updateBtnHandler);
  });
}

function clearInputs() {
  Object.values(inputFields).forEach(element => {
    element.value = "";
  });
}

function checkCorrectInputs() {
  let values = Object.values(inputFields);
  for (const item of values) {
    if (item.value === "") {
      return false;
    }
  }
  return true;
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
