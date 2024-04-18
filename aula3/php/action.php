<?php

session_start();
include("connect.php");

$username = mysqli_real_escape_string($con,$_POST["username"]);
$password = mysqli_real_escape_string($con,$_POST["password"]);

if(empty($_POST["username"]) || empty($_POST["password"])){
    header("location: index.html");
    exit();
};

$query = "select * from user_user where username = '$username' and passw = '$password'";

echo $query;

$result = mysqli_query($con, $query);

$row = mysqli_num_rows($result);

echo $row;

?>