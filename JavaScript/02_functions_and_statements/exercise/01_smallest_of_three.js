function findSmallest(...args) {
  let smallestNumber = Math.min(...args);
  
  return smallestNumber;
}

console.log(findSmallest(2, 3, 5));