const btnCambiarTitulo = document.getElementById("cambiar_titulo");
btnCambiarTitulo.addEventListener("click", () => {
  const inputNuevoTitulo = document.getElementById("nuevo_titulo");
  const nuevoTitulo = inputNuevoTitulo.value;
  document.title = nuevoTitulo;
});