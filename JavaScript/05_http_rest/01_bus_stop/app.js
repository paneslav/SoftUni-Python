async function getInfo() {
  const BASE_URL = "http://localhost:3030/jsonstore/bus/businfo/";
  const inputArea = document.getElementById("stopId");
  let stopId = inputArea.value;
  let searchedUrl = `${BASE_URL}${stopId}`;

  let stopName = document.getElementById("stopName");
  let buses = document.getElementById("buses");

  try {
    let response = await fetch(searchedUrl);
    let result = await response.json();

    stopName.textContent = result.name;

    for (bus in result.buses) {
      let newLi = document.createElement("li");
      newLi.textContent = `Bus ${bus} arrives in ${result.buses[bus]} minutes`;
      buses.appendChild(newLi);
    }
  } catch (error) {
    stopName.textContent = "Error";
  }
}
