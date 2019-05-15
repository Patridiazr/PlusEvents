function checkRut(rut) {

     // Despejar Puntos
     var valor = rut.value.replace('.','');
     // Despejar Guión
     valor = valor.replace('-','');
    
     // Aislar Cuerpo y Dígito Verificador
     cuerpo = valor.slice(0,-1);
     dv = valor.slice(-1).toUpperCase();
    
     // Formatear RUN
     rut.value = cuerpo + '-'+ dv
    
     // Si no cumple con el mínimo ej. (n.nnn.nnn)
     if(cuerpo.length < 7) { rut.setCustomValidity("RUT Incompleto"); return false;}
    
     // Calcular Dígito Verificador
     suma = 0;
     multiplo = 2;
    
     // Para cada dígito del Cuerpo
     for(i=1;i<=cuerpo.length;i++) {
    
         // Obtener su Producto con el Múltiplo Correspondiente
         index = multiplo * valor.charAt(cuerpo.length - i);
        
         // Sumar al Contador General
         suma = suma + index;
        
         // Consolidar Múltiplo dentro del rango [2,7]
         if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
  
     }
    
     // Calcular Dígito Verificador en base al Módulo 11
     dvEsperado = 11 - (suma % 11);
    
     // Casos Especiales (0 y K)
     dv = (dv == 'K')?10:dv;
     dv = (dv == 0)?11:dv;
    
     // Validar que el Cuerpo coincide con su Dígito Verificador
     if(dvEsperado != dv) { rut.setCustomValidity("RUT Inválido"); return false; }
    
     // Si todo sale bien, eliminar errores (decretar que es válido)
     rut.setCustomValidity('');
 }

 $("#form1").validate({
    rules: {
        pass1: { 
          required: true,
             minlength: 6,
             maxlength: 10,

        } , 

            pass2: { 
             equalTo: "#pass1",
              minlength: 6,
              maxlength: 10
        }


    },
messages:{
  pass1: { 
          required:"Password Requerido",
          minlength: "Minimo 6 caracteres",
          maxlength: "Maximo 10 caracteres"
        },
}

});



if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/registro/templates/sw.js')
        .then(function() {
            console.log('ServiceWorker registered!');
        })
        .catch(function(err) {
            console.log('ServiceWorker failed :(', err);
        });
    });
  }


  $(document).ready(main);

var contador = 1;


