function makeDict(input) {
  let termDict = {};
  for (const line of input) {
    let pairs = Object.entries(JSON.parse(line));
    for (const [key, value] of pairs) {
      termDict[key] = value
    }
  }

  let sorted = Object.entries(termDict).sort();

  sorted.forEach(element => {
    console.log(`Term: ${element[0]} => Definition: ${element[1]}`)
  });
}

makeDict([
  '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
  '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
  '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
  '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
  '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}',
]);
