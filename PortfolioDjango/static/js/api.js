const formulario= document.getElementById("formContacto")

formulario.addEventListener("submit", e=> {
    e.preventDefault();
     const url= "https://sheetdb.io/api/v1/bxc0vzg9kvfns"

fetch(url, {
    method: 'POST',
    headers: {
        "Content-Type": "application/json",
    },
    
    body: JSON.stringify({ 
      
        data: [ 
            {nombre: nombreform.value,           
            apellido:  apellidoform.value,
            telefono: telefonoform.value,
            mail: mailform.value,
            mensaje: mensajeform.value,}
        ],
     })
})

.then(res => res.json())
.then(res=> {
      console.log(res);
});

    console.log ('Formulario enviado')
    formContacto.reset ();

});


