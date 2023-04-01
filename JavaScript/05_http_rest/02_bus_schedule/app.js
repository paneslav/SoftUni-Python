function solve() {
  const BASE_URL = "http://localhost:3030/jsonstore/bus/schedule/";
  const outputField = Array.from(document.getElementsByClassName("info"))[0];
  const departButton = document.getElementById("depart");
  const arriveButton = document.getElementById("arrive");

  let nextStop = "depot";
  let stopName = "";

  async function depart() {
    try {
      let getRequest = await fetch(`${BASE_URL}${nextStop}`);
      let response = await getRequest.json();

      stopName = response.name;
      nextStop = response.next;

      outputField.textContent = `Next stop ${stopName}`;
      departButton.setAttribute("disabled", true);
      arriveButton.removeAttribute("disabled");
    } catch (error) {
      outputField.textContent = "Error";
      departButton.setAttribute("disabled", true);
      arriveButton.setAttribute("disabled", true);
    }
  }

  async function arrive() {
    outputField.textContent = `Arriving at ${stopName}`;

    arriveButton.setAttribute("disabled", true);
    departButton.removeAttribute("disabled");
  }

  return {
    depart,
    arrive,
  };
}

let result = solve();
