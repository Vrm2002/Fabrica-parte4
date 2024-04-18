<?php

$nome = $_POST["nome"];
$sistema = $_POST["sistema"];
$prof = $_POST["prof"];


echo "O nome digitado foi $nome e $sistema<br>";

for ($i=0;$i<count($prof);$i++){
    echo "$prof[$i]<br>";
}

?>