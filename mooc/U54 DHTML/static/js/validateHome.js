function validateHome(form) {
	var retorno = true;

	if(form["post"].value.trim() == "") {
		alert("Enter a new post")
		form["post"].focus()
		retorno = false;
	}
		
	return(retorno);
}
