function showLot(input) {
  let parkingLot = [];

  for (const item of input) {
    [direction, carNumber] = item.split(", ");

    if (direction === "IN" && !parkingLot.includes(carNumber)) {
      parkingLot.push(carNumber);
    } else if (direction === "OUT" && parkingLot.includes(carNumber)) {
      parkingLot.splice(parkingLot.indexOf(carNumber), 1);
    }
  }

  let sorted = parkingLot.sort();

  if (parkingLot.length === 0) {
    console.log("Parking Lot is Empty");
  } else {
    console.log(sorted.join("\n"));
  }
}

showLot([
  "IN, CA2844AA",
  "IN, CA1234TA",
  "OUT, CA2844AA",
  "IN, CA9999TT",
  "IN, CA2866HI",
  "OUT, CA1234TA",
  "IN, CA2844AA",
  "OUT, CA2866HI",
  "IN, CA9876HH",
  "IN, CA2822UU",
]);

showLot(["IN, CA2844AA", "IN, CA1234TA", "OUT, CA2844AA", "OUT, CA1234TA"]);
