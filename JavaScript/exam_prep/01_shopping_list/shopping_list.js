function goShopping(input) {
  let groceryList = input.shift().split("!");

  operations = {
    Urgent: urgent,
    Unnecessary: unnecessary,
    Correct: correct,
    Rearrange: rearrange,
  };

  for (const item of input) {
    if (item === "Go Shopping!") {
      break;
    }

    let [command, ...groceries] = item.split(" ");

    operations[command](groceries);
    console.log(groceryList);
  }

  console.log(groceryList.join(", "));

  function urgent(item) {
    item = item[0];

    if (groceryList.includes(item)) {
      return;
    }

    groceryList.unshift(item);
  }

  function unnecessary(item) {
    item = item[0];

    if (!groceryList.includes(item)) {
      return;
    }
    let itemIndex = groceryList.indexOf(item);
    groceryList.splice(itemIndex, 1);
  }

  function correct([oldName, newName]) {
    if (!groceryList.includes(oldName)) {
      return;
    }
    let itemIndex = groceryList.indexOf(oldName);
    groceryList.splice(itemIndex, 1, newName);
  }

  function rearrange(item) {
    item = item[0];
    if (!groceryList.includes(item)) {
      return;
    }
    let itemIndex = groceryList.indexOf(item);
    groceryList.splice(itemIndex, 1);
    groceryList.push(item);
  }
}

goShopping([
  "Tomatoes!Potatoes!Bread",
  "Urgent Eggs",
  "Unnecessary Bread",
  "Rearrange Eggs",
]);

goShopping([
  "Milk!Pepper!Salt!Water!Banana",
  "Urgent Salt",
  "Unnecessary Grapes",
  "Correct Pepper Onion",
  "Rearrange Grapes",
  "Correct Tomatoes Potatoes",
  "Go Shopping!",
]);
