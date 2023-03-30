function towns(towns) {
  let townsCollection = {};

  for (const town of towns) {
    let townInfo = town.split(" | ");
    let townName = townInfo[0];
    let latitude = Number(townInfo[1]);
    let longitude = Number(townInfo[2]);

    townsCollection[townName] = {
      town: `${townName}`,
      latitude: `${latitude.toFixed(2)}`,
      longitude: `${longitude.toFixed(2)}`,
    };
  }
  
  let values = Object.values(townsCollection);

  values.forEach(item => {
    console.log(item);
  });
}

towns(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
