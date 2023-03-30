function showChars(charsInfo) {
  let chars = [];

  for (const char of charsInfo) {
    [heroName, level, items] = char.split(" / ");
    // items = items.split(", ");

    let character = { Hero: heroName, level: Number(level), items: items };
    chars.push(character);
  }

  // let sorted = chars.sort((a,b) => (a.level > b.level) ? 1 : (a.level < b.level) ? -1 : 0);
  let sorted = chars.sort((a, b) => a.level - b.level);

  sorted.forEach((element) => {
    let entries = Object.entries(element);

    for (const [key, value] of entries) {
      if (key === "Hero") {
        console.log(`${key}: ${value}`);
      } else {
        console.log(`${key} => ${value}`);
      }
      
    }
  });
}

showChars([
  "Isacc / 25 / Apple, GravityGun",
  "Derek / 12 / BarrelVest, DestructionSword",
  "Hes / 1 / Desolator, Sentinel, Antara",
]);

showChars([
  "Batman / 2 / Banana, Gun",
  "Superman / 18 / Sword",
  "Poppy / 28 / Sentinel, Antara",
]);
