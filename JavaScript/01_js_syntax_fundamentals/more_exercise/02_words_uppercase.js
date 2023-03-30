function transformToUpper(text) {
  let pattern = /[A-Za-z]+/g;
  let matches = text.matchAll(pattern);
  let result = [];

  for (const match of matches) {
    result.push(match[0].toUpperCase());
  }

  console.log(result.join(", "));
}

transformToUpper("dobre,be,ti kolko trq da si tup02");
