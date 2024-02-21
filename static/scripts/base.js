const btn_close = document.querySelector(".close")
const btn_menu = document.querySelector(".menu")
const header = document.querySelector("header")


const display_fn = () => {

    const currentDisplay = header.style.display;
    header.style.display = currentDisplay == "none" ? "flex" : "none"
}
btn_close.addEventListener("click", display_fn)
btn_menu.addEventListener("click", display_fn)