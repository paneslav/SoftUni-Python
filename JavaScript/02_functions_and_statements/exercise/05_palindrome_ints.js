function isPalindrome(numbers) {
  let numsAsString = numbers.map(x => x.toString());

  for (item of numsAsString) {
    let reversedString = item.split("").reverse().join("");
    if (item === reversedString) {
      console.log("true");
    } else {
      console.log("false");
    }
  }
}

isPalindrome([123, 323, 421, 121]);