function validateEditProfile(form) {
	var retorno = true;

	if(form["nickname"].value.trim() == "") {
		alert("Nickname is required")
		form["nickname"].focus()
		retorno = false;
	}
	else if(form["friends"]) {
		
		// funcion que valida el numero de amigos seleccionados, solo pueden ser 2 seleccionados, si son mas o menos, mostramos mensaje de error
		var amigos = 0
		var opciones = document.getElementById('friends').options
		for (var i = 0; i < opciones.length; i++) {
			if (opciones[i].selected)
				amigos++
		}
		if (amigos !== 2) {
			alert("Alerta: Selecciona solo dos amigos")
			form["friends"].focus()
			retorno = false;
		}
	}
	if(form["passwd"].value.trim() == "") {
		alert("Password is required")
		form["passwd"].focus()
		retorno = false;
	}
	else if(form["passwd"].value != form["confirm"].value) {
		alert("Password and Repeat Password are not equal")
		form["passwd"].focus()
		retorno = false;
	} 
	
	return(retorno);
}
