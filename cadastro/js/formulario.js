const form = document.getElementById("formulario");

form.addEventListener('submit', (event)=>{

    event.preventDefault();

    const nome = document.getElementById("inputName");
    const fone = document.getElementById("inputFone");
    const sexo = document.getElementById("sex");

    if(nome.value == ""){
        alert("Digite seu nome.")
        nome.focus();
    }

    if(fone.value.length < 9){
        alert("Digite um número de telefone válido.")
        fone.focus();
    }

    console.log(nome);
    event.target.submit();
})