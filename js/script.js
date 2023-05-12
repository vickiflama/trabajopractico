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

// let menu = document.getElementById("botonHamburguesa");
// let navegador = document.getElementById("menuHamburguesa");

// menu.addEventListener("click", function() {
//     menu.classList.toggle("close");
//     navegador.classList.toggle("show");
// })

// navegador.addEventListener("click", function(){
//     if (e.target.id === "menuHamburguesa") {
//         navegador.classList.toggle.remove("show");
//         menu.classList.toggle.remove("close");
//     }
// })


// document.getElementById("botonHamburguesa").addEventListener("click", function () {
//     var menu = document.getElementById("menuHamburguesa");
//     if (menu.style.display === "none") {
//       menu.style.display = "block";
//     } else {
//       menu.style.display = "none";
//     }
//   });