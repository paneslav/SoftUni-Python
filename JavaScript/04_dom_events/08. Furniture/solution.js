function solve() {
  let inputArea = document.querySelector(
    "#exercise > textarea:nth-child(even)"
  );
  let outputArea = document.querySelector(
    "#exercise > textarea:nth-child(odd)"
  );

  let generateButton = document.querySelector("button:nth-child(odd)");
  let buyButton = document.querySelector("button:nth-child(even)");

  let tableBody = document.getElementsByTagName("tbody")[0];
  let checkboxes = [];

  generateButton.addEventListener("click", generateFurniture);
  buyButton.addEventListener("click", buyFurniture);

  function generateFurniture(e) {
    const furnitures = JSON.parse(inputArea.value);

    // fill rows
    for (const item of furnitures) {
      let entries = Object.entries(item);
      let newRow = document.createElement("tr");
      let newCheckbox = document.createElement("input");
      let newData = document.createElement("td");
      tableBody.appendChild(newRow);

      // fill table data
      for (const [key, value] of entries) {
        let newElement;
        let newData = document.createElement("td");
        newRow.appendChild(newData);

        if (key === "img") {
          newElement = document.createElement("img");
          newData.appendChild(newElement);

          newElement.src = value;
        } else {
          newElement = document.createElement("p");
          newData.appendChild(newElement);

          newElement.textContent = value;
        }
      }

      // add checkbox
      newData.appendChild(newCheckbox);
      newCheckbox.setAttribute("type", "checkbox");
      newRow.appendChild(newData);
      checkboxes.push(newCheckbox);
    }
  }

  function buyFurniture(e) {
    let cart = [];
    let totalPrice = 0;
    let totalDecFactor = 0;
    let averageDecFactor = 0;
    let markedBoxes = checkboxes.filter((a) => a.checked === true);

    for (const cb of markedBoxes) {
      let children = Array.from(cb.parentNode.parentNode.children);
      let name = children[1].textContent;
      let price = Number(children[2].textContent);
      let decorationFactor = Number(children[3].textContent);

      cart.push(name);
      totalPrice += price;
      totalDecFactor += decorationFactor;
    }

    averageDecFactor = totalDecFactor / cart.length;

    outputArea.value = `Bought furniture: ${cart.join(
      ", "
    )}\nTotal price: ${totalPrice.toFixed(
      2
    )}\nAverage decoration factor: ${averageDecFactor}`;
  }
}
