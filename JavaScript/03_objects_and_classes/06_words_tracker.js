function trackWord([words, ...wordPool]) {
  function countInstances(word) {
    let count = 0;

    wordPool.forEach((element) => {
      if (element === word) {
        count += 1;
      }
    });

    return count;
  }

  let result = {};
  words = words.split(" ");

  for (const word of words) {
    result[word] = countInstances(word);
  }

  let sortedByOccurence = Object.entries(result).sort((a, b) => {
    return b[1] - a[1];
  });

  sortedByOccurence.forEach((item) => {
    console.log(`${item[0]} - ${item[1]}`);
  });
}

trackWord([
  "this sentence",
  "In",
  "this",
  "sentence",
  "you",
  "have",
  "to",
  "count",
  "the",
  "occurrences",
  "of",
  "the",
  "words",
  "this",
  "and",
  "sentence",
  "because",
  "this",
  "is",
  "your",
  "task",
]);

trackWord([
  "is the",
  "first",
  "sentence",
  "Here",
  "is",
  "another",
  "the",
  "And",
  "finally",
  "the",
  "the",
  "sentence",
]);
