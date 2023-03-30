function fromTo(startSym, endSym) {
  let result = [];
  let start = startSym.charCodeAt(0);
  let end = endSym.charCodeAt(0);


  if (end > start) {
    for (let i = start + 1; i < end; i++) {
      const value = i;
      result.push(String.fromCharCode(value));
    }
  } else {
    for (let i = end + 1; i < start; i++) {
      const value = i;
      result.push(String.fromCharCode(value));
    }
  }

  return result.join(' ');
}

console.log(fromTo("a", "d"));
