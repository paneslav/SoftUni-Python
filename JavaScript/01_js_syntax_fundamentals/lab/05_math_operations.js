let operations = {
    "+": (a, b) => {return a + b},
    "-": (a, b) => {return a - b},
    "*": (a, b) => {return a * b},
    "/": (a, b) => {return a / b},
    "%": (a, b) => {return a % b},
    "**": (a, b) => {return a ** b}
}


function solve(num1, num2, operator) {
    result = operations[operator](num1, num2);
    console.log(result);
}

solve(5, 6, "+")
solve(5, 6, "-")
solve(5, 6, "*")
solve(5, 6, "/")
solve(5, 6, "%")
solve(5, 6, "**")