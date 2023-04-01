function attachEvents() {
  const MSG_URL = "http://localhost:3030/jsonstore/messenger";
  const sendButton = document.getElementById("submit");
  const refreshButton = document.getElementById("refresh");
  const textArea = document.getElementById("messages");
  const nameArea = Array.from(document.getElementsByTagName("input"))[0];
  const msgArea = Array.from(document.getElementsByTagName("input"))[1];

  sendButton.addEventListener("click", sendHandler);
  refreshButton.addEventListener("click", refreshHandler);

  async function sendHandler() {
    let message = {
      author: nameArea.value,
      content: msgArea.value,
    };

    const settings = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(message),
    };
    await fetch(MSG_URL, settings);
  }

  async function refreshHandler() {
    textArea.textContent = "";
    let output = [];
    let request = await fetch(MSG_URL);
    let msgList = await request.json();

    for (const msg in msgList) {
      output.push(`${msgList[msg].author}: ${msgList[msg].content}`);
    }
    textArea.textContent = output.join("\n");
  }
}

attachEvents();
