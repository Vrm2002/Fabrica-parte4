<!-- O código deve ser fechado por setas e interrogação, principalmente no HTML -->
<?php 
echo "Olá Senac <br>";

// comentários no php são assim
#assim
/* assim */


$num1 = 10;
$num2 = 20;
$soma = $num1+$num2;

echo "<br> a soma de $num1+$num2=$soma <br>"; //echo é para printar



/* funções */

$x = 35.52;
$z = -40;


Abs($z); #Tranforma em um valor absoluto.
Pow($x,2); #Potenciação.
Sqrt($x); #Raiz quadrada.
Round($x); #Arredonda.
Intval($x); #Pega o numero inteirol.
Number_format($x,2,",","."); #Substitui o ultimo simbolo informado pelo primeiro. Altera as casas decimais.

/* vetores */

$nota=[];
$nota[0] = 7;
$nota[1] = 8;
$nota[2] = 9;
$nota[3] = 10;
$nota[4] = 11;

echo "<br> A nota 1 é = $nota[1] <br>";

$media = ($nota[0] + $nota[1] + $nota[2] + $nota[3] + $nota[4])/5;

echo "<br> A média é: ".$media."<br>";

$situacao = $media >=6?"Aprovado":"Reprovado";

echo "<br> Situação: ".$situacao."<br>";


/* do While */

$i = 0; #O teste da condição é feito depois de executar o código.

do{
    echo $i;
    $i++;
}while($i<=10)
?>

