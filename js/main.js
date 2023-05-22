// Ventana modal 1
var modal1 = document.getElementById("ventanaModal1");

// Botón que abre el modal
var boton1 = document.getElementById("abrirModal1");

// Hace referencia al elemento <span> que tiene la X que cierra la ventana

var span1 = document.getElementsByClassName("cerrar1")[0];
// Cuando el usuario hace click en el botón, se abre la ventana

boton1.addEventListener("click",function() {
  modal1.style.display = "block";
});

// Si el usuario hace click en la x, la ventana se cierra
span1.addEventListener("click",function() {
  modal1.style.display = "none";
});

// Si el usuario hace click fuera de la ventana, se cierra.
window.addEventListener("click",function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
});

// Ventana modal 2
var modal2 = document.getElementById("ventanaModal2");
var boton2 = document.getElementById("abrirModal2");
var span2 = document.getElementsByClassName("cerrar2")[0];
boton2.addEventListener("click",function() {
  modal2.style.display = "block";
});
span2.addEventListener("click",function() {
  modal2.style.display = "none";
});
window.addEventListener("click",function(event) {
  if (event.target == modal2) {
    modal2.style.display = "none";
  }
});




// Ventana modal 3
var modal3 = document.getElementById("ventanaModal3");
var boton3 = document.getElementById("abrirModal3");
var span3 = document.getElementsByClassName("cerrar3")[0];
boton3.addEventListener("click",function() {
  modal3.style.display = "block";
});
span3.addEventListener("click",function() {
  modal3.style.display = "none";
});
window.addEventListener("click",function(event) {
  if (event.target == modal3) {
    modal3.style.display = "none";
  }
});

// Ventana modal 4
var modal4 = document.getElementById("ventanaModal4");
var boton4 = document.getElementById("abrirModal4");
var span4 = document.getElementsByClassName("cerrar4")[0];
boton4.addEventListener("click",function() {
  modal4.style.display = "block";
});
span4.addEventListener("click",function() {
  modal4.style.display = "none";
});
window.addEventListener("click",function(event) {
  if (event.target == modal4) {
    modal4.style.display = "none";
  }
});