let operations = {
    "+": (a, b) => {return a + b},
    "-": (a, b) => {return a - b},
    "*": (a, b) => {return a * b},
    "/": (a, b) => {return a / b},
    "%": (a, b) => {return a % b},
    "**": (a, b) => {return a ** b}
}


function solve(num1, operator, num2) {
    result = operations[operator](num1, num2);
    console.log(result);
}

solve(5, "+", 10);
solve(6, "-", 2)
