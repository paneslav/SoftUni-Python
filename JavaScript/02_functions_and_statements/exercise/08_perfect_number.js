function isNumPerfect(num) {
  let divisors = [];

   for (let i = 1; i < num; i++) {
    if (num % i === 0) {
      divisors.push(i);
    }
   }

   let sum = divisors.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

   if (num === sum) {
    console.log("We have a perfect number!")
   } else {
    console.log("It's not so perfect.")
   }
}

isNumPerfect(123);