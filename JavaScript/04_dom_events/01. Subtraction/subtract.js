function subtract() {
    let firstNum = document.getElementById("firstNumber").value;
    let secondNum = document.getElementById("secondNumber").value;
    let result;

    firstNum = Number(firstNum);
    secondNum = Number(secondNum);

    result = firstNum - secondNum;
    document.getElementById("result").textContent = result;
}