function validatePass(password) {
  var minLength = 6;
  var maxLength = 10;

  if (lengthCheck() && digitsAndLettersOnly() && twoDigits()) {
    console.log("Password is valid");
    return;
  }

  if (lengthCheck() === false) {
    console.log("Password must be between 6 and 10 characters");
  }

  if (digitsAndLettersOnly() === false) {
    console.log("Password must consist only of letters and digits");
  }

  if (twoDigits() === false) {
    console.log("Password must have at least 2 digits");
  }


  function lengthCheck() {
    return Boolean(password.length >= minLength && password.length <= maxLength);
  }

  function digitsAndLettersOnly() {
    return Boolean(password.match(/^[A-Za-z0-9]*$/));
  }

  function twoDigits() {
    return Boolean(password.match(/(\D*\d){2,}/))
  }
}

validatePass("Pa$s$s");