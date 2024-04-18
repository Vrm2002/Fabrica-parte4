<?php

session_start();
include("connect.php");

$user = mysqli_real_escape_string($con, $_POST["login"]);
$passw = mysqli_real_escape_string($con, $_POST["password"]);

if(empty($_POST["login"]) || empty($_POST["password"])){

    header("location: index.html");
    exit();

}else{

    $query = "select * from user_user where login = '$user' and senha = '$passw'";
    $result = mysqli_query($con, $query);
    $row = mysqli_num_rows($result);
    $retorno = mysqli_fetch_array($result);
    
    if($row == 0){

        header("location:index.html");
        exit();

    }else if($row == 1){
        $_SESSION['nome'] = $user;
        $_SESSION['setor'] = $retorno['setor'];

        if($_SESSION['setor'] == 'admin'){
            header('location:adm.php');
            exit();
        }
        else if($_SESSION['setor'] =='suporte'){
            header('location:suporte.php');
            exit();
        }
    }
}

