
  // Obtener el botón de despliegue
const toggleBtn = document.querySelector('.toggle-menu');

// Obtener el menú
const menu = document.querySelector('.menu');

// Agregar evento click al botón de despliegue
toggleBtn.addEventListener('click', () => {
  menu.classList.toggle('active');
});






//Reloj - Banner

function getTime() {
    const date = new Date();
    const options = { timeZone: 'America/Santiago', hour12: false };
    const time = date.toLocaleTimeString('en-US', options);
    document.getElementById('time').textContent = time;
  }

  setInterval(getTime, 1000);



//api



$(document).ready(function() {
    $("#toggleBtn").click(function() {
      $("#feriadosContainer").toggle();
  
      if ($("#feriadosContainer").is(":visible")) {
        loadFeriados();
        $("#toggleBtn").val("Ocultar Feriados");
      } else {
        $("#categorias tbody").empty();
        $("#toggleBtn").val("Mostrar Feriados");
      }
    });
  
    $("#hideBtn").click(function() {
      $("#feriadosContainer").hide();
      $("#toggleBtn").val("Mostrar Feriados");
    });
  });
  
  function loadFeriados() {
    $.get("https://www.feriadosapp.com/api/laws.json", function(data) {
      $.each(data.data, function(i, item) {
        $("#categorias").append("<tr><td>" + item.title + "</td><td>" + item.date + "</td></tr>");
      });
    });
  }

  


/*subir y bajar boton*/
$(document).ready(function() {
    $(window).scroll(function() {
      if ($(this).scrollTop() > 100) {
        $('#scrollToTopBtn').fadeIn();
      } else {
        $('#scrollToTopBtn').fadeOut();
      }
  
      if ($(this).scrollTop() < $(document).height() - $(window).height() - 100) {
        $('#scrollToBottomBtn').fadeIn();
      } else {
        $('#scrollToBottomBtn').fadeOut();
      }
    });
  
    $('#scrollToTopBtn').click(function() {
      $('html, body').animate({ scrollTop: 0 }, 'slow');
      return false;
    });
  
    $('#scrollToBottomBtn').click(function() {
      $('html, body').animate({ scrollTop: $(document).height() - $(window).height() }, 'slow');
      return false;
    });
  });
  







//valoracion falsa

document.addEventListener("DOMContentLoaded", function() {
  // Genera la valoración falsa de usuario para cada producto
  var products = document.querySelectorAll(".product");

  products.forEach(function(product) {
    var rating = product.querySelector(".rating");
    var stars = rating.querySelectorAll(".star");
    var score = Math.random() * 10; // Puntuación aleatoria de 0 a 5

    stars.forEach(function(star, index) {
      if (index < Math.floor(score)) {
        star.classList.add("filled");
      } else if (index === Math.floor(score) && score % 1 !== 0) {
        star.classList.add("half-filled");
      }
    });

    var ratingScore = document.createElement("span");
    ratingScore.classList.add("rating-score");
    ratingScore.textContent = score.toFixed(1); // Redondea el puntaje a 1 decimal
    rating.appendChild(ratingScore);
  });
});






// tienda contacto

$(function(){
  $("#mi-formulario").validate({

      rules:{
          nom:{
              required:true
          },
          correo:{
              required:true,
              email:true
          },
          fono:{
              required:true
          },
          pass:{
              required:true
          },
          fecha:{
              required:true
          },
          pass2:{
              required:true,
              equalTo:pass
          },
      },//rules
      messages:{
          nom:{
              required:'Ingrese nombre de usuario',
              minlength:'Caracteres insuficientes (3)'
          },
          correo:{
              required:'Ingrese correo electrónico',
              email:'Formato de correo no válido'
          },
          fono:{
              required:'Ingrese número de teléfono',
              minlength:'Digitos insuficientes (9)'
          },
          fecha:{
              required:'Ingrese una fecha',
              min:'Seleccione una fecha válida'
          },
          pass:{
              required: 'Ingrese una contraseña',
              minlength: 'Caracteres insuficientes(8)'
          },
          pass2:{
              required:'Reingrese contraseña',
              minlength: 'Caracteres insuficientes(8)',
              equalTo:'Contraseñas no coinciden'
          }
      },
  })
});