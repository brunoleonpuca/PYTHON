// Creamos funcion para interactuar desde el formulario con los elementos del HTML
function sumar (form) {
    form.resultado.value = Number(form.num1.value) + Number(form.num2.value)
}

// Creamos variable y funcion para interactuar con las acciones de los elementos del HTML y selectores del CSS
const btn = document.querySelector('.change-body');

btn.addEventListener('click', () => {
    document.body.classList.toggle('changecolor');
});

