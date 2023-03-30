function solve() {
  const inputArea = document.getElementById("input");
  const outputArea = document.getElementById("output");

  let text = inputArea.value.split(".");
  text.pop();
  let children = outputArea.children;

  for (const sentence of text) {
    addTextToParagraph(sentence);
  }

  function addTextToParagraph(text) {
    if (children.length === 0) {
      outputArea.appendChild(document.createElement("p"));
    }

    let currentParagraph = children[children.length - 1];
    if (currentParagraph.textContent.split(".").length === 4) {
      currentParagraph = outputArea.appendChild(document.createElement("p"));
    }

    currentParagraph.textContent += text + ".";
  }
}
