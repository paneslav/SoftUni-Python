function draw(x) {
  let result = [];

  for (let i = 0; i < x; i++) {
    result.push(x);
    }
  
  for (let i = 0; i < x; i++) {
    console.log(result.join(" "))
  }

}

draw(7);