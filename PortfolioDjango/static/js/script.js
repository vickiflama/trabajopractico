/// BOTON DARK/LIGHT MODE

let modo=document.getElementById("modo");
let body=document.body;

modo.addEventListener("click", function(){
    let val=body.classList.toggle("dark")
    localStorage.setItem("modo",val)
})

let valor=localStorage.getItem("modo")

if (valor==true) {
    body.classList.add("dark")
} else{
    body.classList.remove("dark")
}


// MENU HAMBURGUESA ///

const navToggle = document.querySelector(".nav-toggle")
const navMenu = document.querySelector(".nav-menu")

navToggle.addEventListener("click", ()=> {
    navMenu.classList.toggle("nav-menu_visible");
})




// ANIMACIONES SKILLS

function mostrarScroll(){
    let animado = document.querySelector(".animado1");
    let scrollTop = document.documentElement.scrollTop;
    let alturaAnimado = animado.offsetTop;
    if (alturaAnimado - 400 < scrollTop) {
        animado.style.opacity = 1;
        animado.classList.add("mostrarArriba");
    }
}
window.addEventListener("scroll", mostrarScroll);



///ANIMADO2
function mostrarScroll2(){
    let animado = document.querySelector(".animado2");
    let scrollTop = document.documentElement.scrollTop;
    let alturaAnimado = animado.offsetTop;
    if (alturaAnimado - 500 < scrollTop) {
        animado.style.opacity = 1;
        animado.classList.add("mostrarArriba");
    }
}
window.addEventListener("scroll", mostrarScroll2);

///ANIMADO3

function mostrarScroll3(){
    let animado = document.querySelector(".animado3");
    let scrollTop = document.documentElement.scrollTop;
    let alturaAnimado = animado.offsetTop;
    if (alturaAnimado - 400 < scrollTop) {
        animado.style.opacity = 1;
        animado.classList.add("mostrarArriba");
    }
}
window.addEventListener("scroll", mostrarScroll3);

//ANIMADO4

function mostrarScroll4(){
    let animado = document.querySelector(".animado4");
    let scrollTop = document.documentElement.scrollTop;
    let alturaAnimado = animado.offsetTop;
    if (alturaAnimado - 400 < scrollTop) {
        animado.style.opacity = 1;
        animado.classList.add("mostrarArriba");
    }
}
window.addEventListener("scroll", mostrarScroll4);



