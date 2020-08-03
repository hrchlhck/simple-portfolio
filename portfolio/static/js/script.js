const getCurrentYear = () => {
    return new Date().getFullYear();
}

const updateFooter = () => {
    const footerText = document.getElementById("footer-text");
    footerText.innerText = "\u00A9 Copyright " + getCurrentYear() + " Pedro Horchulhack";
}

window.onload = () => {
    updateFooter();
}