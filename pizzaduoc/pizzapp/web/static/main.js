
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

