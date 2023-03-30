function create(words) {
  for (const item of words) {
    let div = document.createElement("div");
    let p = document.createElement("p");
    p.textContent = item;
    div.appendChild(p);
    div.addEventListener("click", onClick);
    document.getElementById("content").appendChild(div);
  }

  function onClick(e) {
    let element = e.currentTarget.children[0];
    if (element.style.display === "none") {
      element.style.display = "block";
    } else {
      element.style.display = "none";
    }
  }
}
