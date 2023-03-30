function sortNumbers(arr) {
    let result = [];
    let arrSize = arr.length;
    let sortedArr = arr.sort((a, b) => a - b);
    let firstHalf = sortedArr.splice(0, 5);
    let secondHalf = sortedArr.reverse();
    
    for (let i = 0; i < arrSize; i++) {
        if (i % 2 === 0) {
            result.push(firstHalf.shift());
        } else {
            result.push(secondHalf.shift())
        }
        
    }

    console.log(result.join("\r\n"))
}


sortNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18]);