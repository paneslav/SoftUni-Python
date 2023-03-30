function checkForHash(string) {
  let result = [];
  let strippedString = string.split(" ");

  for (item of strippedString) {
    if (item.startsWith("#") && /^#[a-zA-Z]+$/.test(item) === true) {
      result.push(item.slice(1));
    }
  }

  console.log(result.join("\r\n"));
}

checkForHash("Nowadays everyone uses # to tag a #special word in #socialMedia");
checkForHash("The symbol # is known #variously in English-speaking #regions as the #number sign");
