function lockedProfile() {
    let buttons = document.getElementsByTagName("button");
    for (const button of buttons) {
        button.addEventListener('click', showMore);
    }

    function showMore(e) {
        let element = e.currentTarget;
        let parentChildren = element.parentElement.children;
        let unlockRadio = parentChildren[4];
        let additionalInfo = parentChildren[9];

        if (unlockRadio.checked) {
            if (this.textContent === "Show more") {
                this.textContent = "Hide it";
                additionalInfo.style.display = "block";
            } else {
                this.textContent = "Show more";
                additionalInfo.style.display = "none";
            }
        }
    }
}