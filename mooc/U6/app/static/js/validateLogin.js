function validateLogin(form) {
	var retorno = true;

	if(form["email"].value.trim() == "") {
		alert("Email is required")
		form["email"].focus()
		retorno = false;
	}
	else if(form["passwd"].value.trim() == "") {
		alert("Password is required")
		form["passwd"].focus()
		retorno = false;
	}

	
	return(retorno);
}
