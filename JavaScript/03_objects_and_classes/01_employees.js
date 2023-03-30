function showEmployees(input) {
  let employees = {};
  for (const person of input) {
    let name = person;
    let personalNumber = person.length;
    employees[name] = personalNumber;
  }

  let keys = Object.keys(employees);

  keys.forEach((person) => {
    console.log(`Name: ${person} -- Personal Number: ${employees[person]}`);
  });
}

showEmployees([
  "Silas Butler",
  "Adnaan Buckley",
  "Juan Peterson",
  "Brendan Villarreal",
]);
