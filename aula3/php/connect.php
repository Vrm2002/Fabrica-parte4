<?php

$host = "127.0.0.1";
$usuario = "vinicius";
$senha = "Dragonpapy123.";
$bd = "teste";

$con = new mysqli($host,$usuario,$senha,$bd);

if ($con -> connect_errno){
    echo "Falha na Conexão :(".$con->connect_errno.")".$con -> connect_error;
}else{
    echo $con->host_info."\n";
}


?>