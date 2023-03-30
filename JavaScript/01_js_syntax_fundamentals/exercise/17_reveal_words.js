function revealWords(words, sentence) {
  words = words.split(", ");
  sentence = sentence.split(" ");

  while (words.length > 0) {
    let currentWord = words[0];

    for (item of sentence) {
      if (item.startsWith("*") && item.length === currentWord.length) {
        let itemIndex = sentence.indexOf(item);
        sentence[itemIndex] = currentWord;
        words.shift();
        break;
      }
    }
  }


  console.log(sentence.join(" "));
}

// revealWords(
//   "great",
//   "softuni is ***** place for learning new programming languages"
// );

revealWords(
    "great, learning",
    "softuni is ***** place for ******** new programming languages"
  );