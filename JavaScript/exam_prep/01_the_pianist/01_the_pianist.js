function arrangePieces(input) {
  let n = Number(input.shift());

  let musicCollection = {};

  ///////

  for (let i = 0; i < n; i++) {
    let [piece, composer, key] = input.shift().split("|");
    musicCollection[piece] = { Composer: composer, Key: key };
  }

  ////////

  while (true) {
    let command = input.shift().split("|");

    if (command[0] === "Stop") {
      break;
    }

    if (command[0] === "Add") {
      let [_com, piece, composer, key] = command;

      if (musicCollection.hasOwnProperty(piece)) {
        console.log(`${piece} is already in the collection!`);
        continue;
      }

      musicCollection[piece] = { Composer: composer, Key: key };
      console.log(`${piece} by ${composer} in ${key} added to the collection!`);
    } else if (command[0] === "Remove") {
      let piece = command[1];

      if (!musicCollection.hasOwnProperty(piece)) {
        console.log(
          `Invalid operation! ${piece} does not exist in the collection.`
        );
        continue;
      }
      delete musicCollection[piece];
      console.log(`Successfully removed ${piece}!`);
    } else {
      let [_com, piece, newKey] = command;

      if (!musicCollection.hasOwnProperty(piece)) {
        console.log(
          `Invalid operation! ${piece} does not exist in the collection.`
        );
        continue;
      }

      musicCollection[piece].Key = newKey;
      console.log(`Changed the key of ${piece} to ${newKey}!`);
    }
  }

  /////////

  for (piece in musicCollection) {
    console.log(
      `${piece} -> Composer: ${musicCollection[piece].Composer}, Key: ${musicCollection[piece].Key}`
    );
  }
}

arrangePieces([
  "3",
  "Fur Elise|Beethoven|A Minor",
  "Moonlight Sonata|Beethoven|C# Minor",
  "Clair de Lune|Debussy|C# Minor",
  "Add|Sonata No.2|Chopin|B Minor",
  "Add|Hungarian Rhapsody No.2|Liszt|C# Minor",
  "Add|Fur Elise|Beethoven|C# Minor",
  "Remove|Clair de Lune",
  "ChangeKey|Moonlight Sonata|C# Major",
  "Stop",
]);
