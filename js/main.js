let page_rol = 'nulo';


$("#formIngreso").on("submit", data => {
    let email = data.target[0].value
    let clave = data.target[1].value

    // login forzado 1
    if(email == "correo@admin.cl" & clave == "clave123"){ 
        rol = 'admin';
        window.location.replace("/AdminPage.html")
    } else{return false;}
        
    // login forzado 2
    if(email == "correo@cliente.cl" & clave == "clave321"){ 
        page_rol = 'admin'
        window.location.replace("/main.html")
    } else{return false;} 
    
});

const btn = document.getElementById('btnregistro');

document.getElementById('formRegistro')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Registrando...';

   const serviceID = 'default_service';
   const templateID = 'template_reg_pizza2024';

   emailjs.sendForm(serviceID, templateID, this)
    .then(() => {
      btn.value = 'Cuenta creada';
      alert('Sent!');
    }, (err) => {
      btn.value = 'Error, reintente';
      alert(JSON.stringify(err));
    });
});