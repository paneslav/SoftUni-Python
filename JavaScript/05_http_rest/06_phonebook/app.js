function attachEvents() {
  const PHONE_URL = "http://localhost:3030/jsonstore/phonebook";
  const personArea = document.getElementById("person");
  const phoneArea = document.getElementById("phone");
  const loadBtn = document.getElementById("btnLoad");
  const createBtn = document.getElementById("btnCreate");
  const ul = document.getElementById("phonebook");

  loadBtn.addEventListener("click", loadHandler);
  createBtn.addEventListener("click", createHandler);

  function loadHandler() {
    ul.innerHTML = "";

    fetch(PHONE_URL)
      .then((response) => response.json())
      .then((data) => {
        Object.values(data).forEach((entry) => {
          const li = document.createElement("li");
          li.textContent = `${entry.person}: ${entry.phone}`;
          const btnDelete = document.createElement("button");
          btnDelete.textContent = "Delete";
          btnDelete.addEventListener("click", () =>
            deleteHandler(entry._id, li)
          );
          li.appendChild(btnDelete);
          ul.appendChild(li);
        });
      })
      .catch();
  }
  //   async function loadHandler() {
  //     try {
  //       ul.textContent = "";
  //       let request = await fetch(PHONE_URL);
  //       let phoneBook = await request.json();

  //       for (const key in phoneBook) {
  //         let newLi = document.createElement("li");
  //         newLi.textContent = `${phoneBook[key].person}: ${phoneBook[key].phone}`;

  //         let deleteBtn = document.createElement("button");
  //         deleteBtn.addEventListener("click", () => deleteHandler(key, newLi));
  //         deleteBtn.textContent = "Delete";

  //         newLi.appendChild(deleteBtn);
  //         ul.appendChild(newLi);
  //       }
  //     } catch (err) {
  //       console.error(err);
  //     }
  //   }

  function createHandler() {
    const person = personArea.value.trim();
    const phone = phoneArea.value.trim();

    if (!person || !phone) {
      return;
    }

    const data = { person, phone };

    fetch(PHONE_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    })
      .then(() => {
        personArea.value = "";
        phoneArea.value = "";
        loadHandler();
      })
      .catch();
  }
  //   async function createHandler() {
  //     try {
  //         const person = personArea.value.trim();
  //         const phone = phoneArea.value.trim();

  //         if (!person || !phone) {
  //           return;
  //         }
  //         let contact = {
  //           person,
  //           phone,
  //         };

  //         const settings = {
  //           method: "POST",
  //           headers: { "Content-Type": "application/json" },
  //           body: JSON.stringify(contact),
  //         };
  //         await fetch(PHONE_URL, settings);

  //         personArea.value = "";
  //         phoneArea.value = "";

  //     } catch (err) {
  //         console.error(err);
  //     }
  //   }

  function deleteHandler(key, li) {
    fetch(`${PHONE_URL}/${key}`, {
      method: "DELETE",
    })
      .then(() => li.remove())
      .catch();
  }
}

attachEvents();
