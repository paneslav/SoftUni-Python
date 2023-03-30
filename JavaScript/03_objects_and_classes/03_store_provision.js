function addStock(currentStock, orderedProducts) {
  let inventory = {};

  // Check current stock
  while (currentStock.length !== 0) {
    let product = currentStock.shift();
    let quantity = Number(currentStock.shift());

    if (!inventory.hasOwnProperty(product)) {
      inventory[product] = 0;
    }

    inventory[product] += quantity;
  }

  // Add ordered produts to stock
  while (orderedProducts.length !== 0) {
    let product = orderedProducts.shift();
    let quantity = Number(orderedProducts.shift());

    if (!inventory.hasOwnProperty(product)) {
      inventory[product] = 0;
    }

    inventory[product] += quantity;
  }

  //Print result in format 'Product -> 5'
  let pairs = Object.entries(inventory);

  for (const [key, value] of pairs) {
    console.log(`${key} -> ${value}`)
  }
}

addStock(
  ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
  ["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
);
