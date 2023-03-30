function addItem() {
    let itemText = document.getElementById("newItemText");
    let itemValue = document.getElementById("newItemValue");
    let selectMenu = document.getElementById("menu");
    let newOption = document.createElement("option");
    newOption.textContent = itemText.value;
    newOption.value = itemValue.value;

    selectMenu.appendChild(newOption);
    itemText.value = "";
    itemValue.value = "";

}