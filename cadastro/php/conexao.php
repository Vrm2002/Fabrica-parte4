<?php

$host = '10.28.1.213';
$database = 'cadpessoa';
$username = 'suporte';
$password = 'suporte';

$con = new mysqli($host,$username,$password,$database);

if($con){
    echo "Conectado no banco.";
}else{
    echo "Banco Lixo";
}