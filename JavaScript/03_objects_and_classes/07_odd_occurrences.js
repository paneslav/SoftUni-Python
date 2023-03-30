function checkForOdd(input) {
  let inputToLower = input.toLowerCase();
  let result = [];
  let splitWords = inputToLower.split(" ");

  for (const word of splitWords) {
    let count = splitWords.filter((w) => w === word).length;

    if (count % 2 !== 0 && !result.includes(word)) {
      result.push(word);
    }
  }

  console.log(result.join(" "));
}

checkForOdd("Java C# Php PHP Java PhP 3 C# 3 1 5 C#");
checkForOdd("Cake IS SWEET is Soft CAKE sweet Food");
