function showMovies(input) {
  let movieList = [];

  for (const item of input) {
    let operation = item.match(/(addMovie|directedBy|onDate)/g).join();
    // let operations = item.split(" ");
    let splitBySpace = item.split(" ");

    runOperation(operation, splitBySpace);
  }

  function runOperation(operation, array) {
    if (operation === "addMovie") {
      let movieName = array.slice(1).join(" ");
      let movie = {
        name: movieName,
      };
      movieList.push(movie);
    } else {
      let keyWordIndex = array.indexOf(operation);
      let movieName = array.slice(0, keyWordIndex).join(" ");
      let movie = movieExists(movieName);

      if (movie) {
        let secondHalf = array.slice(keyWordIndex + 1).join(" ");
        let attr = operation === "onDate" ? "date" : "director";
        movie[attr] = secondHalf;
      }
    }

    function movieExists(movieName) {
      let result = movieList.find((item) => item.name === movieName);
      return result;
    }
  }

  movieList.forEach((element) => {
    if (Object.values(element).length === 3) {
      console.log(JSON.stringify(element));
    }
  });
}

// showMovies([
//   "addMovie Fast and Furious",
//   "addMovie Godfather",
//   "Inception directedBy Christopher Nolan",
//   "Godfather directedBy Francis Ford Coppola",
//   "Godfather onDate 29.07.2018",
//   "Fast and Furious onDate 30.07.2018",
//   "Batman onDate 01.08.2018",
//   "Fast and Furious directedBy Rob Cohen",
// ]);

showMovies([
  "addMovie The Avengers",
  "addMovie Superman",
  "The Avengers directedBy Anthony Russo",
  "The Avengers onDate 30.07.2010",
  "Captain America onDate 30.07.2010",
  "Captain America directedBy Joe Russo",
]);
