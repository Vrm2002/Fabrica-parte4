<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>3 Numeros Media</title>
</head>
<body>

<img src="../aaaa.png" alt="aaa">
<br>

<?php

    $val1=10;
    $val2=10;
    $val3=10;
    $media=($val1+$val2+$val3)/3;
    $sit = $media>=7?"Aprovado":"Reprovado";
    $sit2 = $media==10?"com distinção":" ";

    echo "Média: $media <br> Situação: $sit $sit2";


?>

</body>
</html>