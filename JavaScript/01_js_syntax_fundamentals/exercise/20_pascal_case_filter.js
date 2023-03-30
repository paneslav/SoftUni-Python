function capitalSplit(text) {
  let pattern = /(?=[A-Z])/;
  let result = text.split(pattern);

  console.log(result.join(", "));
}

capitalSplit("SplitMeIfYouCanHaHaYouCantOrYouCan");
