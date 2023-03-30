function sortArray(arr) {
  let result = [];
  let sortedArray = arr.sort();

  for (let i = 0; i < sortedArray.length; i++) {
    result.push(`${i + 1}.${sortedArray[i]}`);
  }

  console.log(result.join("\r\n"));
}

sortArray(["John", "Bob", "Christina", "Ema", "Grace", "Bobina"]);
