<?php

include 'conexao.php';

var_dump($_POST);
$nome = $_POST["nome"];
$cpf = $_POST["cpf"];
$fone = $_POST["fone"];
$email = $_POST["email"];

if(isset($_POST['cep'])){ #função isset
    echo "a";
};
if(empty($nome)){ #função empty
    echo "a";
};
if(!empty($nome)){ #função diferente de empty 
    echo "a";
};

$sql = "INSERT INTO pessoa (nome, cpf, fone, email) VALUES ('$nome','$cpf','$fone','$email')";

$result = mysqli_query($con, $sql);

var_dump($result);


if($result){
    echo "CADASTRADO COM SUCESSO";
}else{
    echo "Fracasso";
};


echo "Teu nome ai: $nome";

?>