function checkForSubstring(word, text) {
  text = text.split(" ");
  for (item of text) {
    if (word.toLowerCase() === item.toLowerCase()) {
      console.log(word);
      return;
    }
  }

  console.log(`${word} not found!`)
}

checkForSubstring("python", "JavaScript is the best programming language");
