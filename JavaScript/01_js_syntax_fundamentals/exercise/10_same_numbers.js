function sameNumbers(number) {
  let numToString = String(number);
  let areSame = true;
  let firstDigit = numToString[0];
  let digitsSum = Number(firstDigit);

  for (let i = 1; i < numToString.length; i++) {
    const digit = numToString[i];
    digitsSum += Number(digit);

    if (digit !== firstDigit) {
      areSame = false;
    }
  }

  if (!areSame) {
    console.log("false");
  } else {
    console.log("true");
  }

  console.log(digitsSum);
}

sameNumbers(2222222);
sameNumbers(1234);



// function allEqual(arr) {
//     return new Set(arr).size == 1;
//   }
  
//   allEqual(['a', 'a', 'a', 'a']); // true
//   allEqual(['a', 'a', 'b', 'a']); // false