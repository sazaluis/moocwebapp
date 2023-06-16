function validateProfile(form) {
	var retorno = true;

	if(form["nickname"].value.trim() == "") {
		alert("Nickname is required")
		form["nickname"].focus()
		retorno = false;
	}
	else if(form["email"].value.trim() == "") {
		alert("Email is required")
		form["email"].focus()
		retorno = false;
	}
	else if(form["passwd"].value.trim() == "") {
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
