

//  $("#form1").validate({
//     rules: {
//         pass1: { 
//           required: true,
//              minlength: 6,
//              maxlength: 10,

//         } , 

//             pass2: { 
//              equalTo: "#pass1",
//               minlength: 6,
//               maxlength: 10
//         }


//     },
// messages:{
//   pass1: { 
//           required:"Password Requerido",
//           minlength: "Minimo 6 caracteres",
//           maxlength: "Maximo 10 caracteres"
//         },
// }

// });




function usu(){
    $.ajax ({
        url : "http://127.0.0.1:8000/api/usuario/",
        data : null,
        type : 'GET',
        
        success : function(usuario){
        usuario.forEach(persona => {
            console.log(persona.username)
        });
        },
        error : function(error){
        alert("mal")
        }
        

    })
}