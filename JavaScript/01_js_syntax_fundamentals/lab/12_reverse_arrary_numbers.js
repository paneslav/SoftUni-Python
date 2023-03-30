function solve(n, arr) {
    let newArr = arr.slice(0, n);
    console.log(...newArr.reverse());
}



solve(3, [10, 20, 30, 40, 50])
solve(4, [-1, 20, 99, 5])