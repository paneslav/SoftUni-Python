function attachEvents() {
  const iconMap = {
    Sunny: "☀",
    "Partly sunny": "⛅",
    Overcast: "☁",
    Rain: "☂",
    Degrees: "°",
  };

  const LOCATIONS_URL = "http://localhost:3030/jsonstore/forecaster/locations";
  const TODAY_URL = "http://localhost:3030/jsonstore/forecaster/today/";
  const THREE_DAY_URL = "http://localhost:3030/jsonstore/forecaster/upcoming/";

  const submitButton = document.getElementById("submit");
  const locationField = document.getElementById("location");
  const forecastDiv = document.getElementById("forecast");
  const currentDiv = document.getElementById("current");
  const upcomingDiv = document.getElementById("upcoming");
  submitButton.addEventListener("click", generateWeather);

  async function generateWeather() {
    let locationCode = "";

    let request = await fetch(LOCATIONS_URL);
    let locationsData = await request.json();

    for (const location of locationsData) {
      if (location.name === locationField.value) {
        locationCode = location.code;
      }
    }

    // fill current div
    request = await fetch(`${TODAY_URL}${locationCode}`);
    let todayData = await request.json();

    let cityName = todayData.name;
    let { condition, high, low } = todayData.forecast;

    let newDiv = createElement("div", "", currentDiv, "forecasts");
    let newSpan = createElement(
      "span",
      iconMap[condition],
      newDiv,
      "condition symbol"
    );
    newSpan = createElement("span", "", newDiv, "condition");
    let nestedSpan = createElement(
      "span",
      `${cityName}`,
      newSpan,
      "forecast-data"
    );
    nestedSpan = createElement(
      "span",
      `${low}${iconMap["Degrees"]}/${high}${iconMap["Degrees"]}`,
      newSpan,
      "forecast-data"
    );
    nestedSpan = createElement(
      "span",
      `${condition}`,
      newSpan,
      "forecast-data"
    );

    // fill three-day div
    request = await fetch(`${THREE_DAY_URL}${locationCode}`);
    let threeDayData = await request.json();

    newDiv = createElement("div", "", upcomingDiv, "forecast-info");

    for (const item of threeDayData.forecast) {
        newSpan = createElement("span", "", newDiv, "upcoming");
        let { condition, high, low } = item;
        nestedSpan = createElement("span", `${iconMap[condition]}`, newSpan, "symbol");
        nestedSpan = createElement("span", `${low}${iconMap["Degrees"]}/${high}${iconMap["Degrees"]}`, newSpan, "forecast-data");
        nestedSpan = createElement("span", `${condition}`, newSpan, "forecast-data");

    }

    forecastDiv.style.display = "block";
  }

  function createElement(type, content, parent, classNames) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (parent) {
      parent.appendChild(htmlElement);
    }

    if (classNames) {
      htmlElement.classList.add(...classNames.split(" "));
    }

    return htmlElement;
  }
}

attachEvents();
