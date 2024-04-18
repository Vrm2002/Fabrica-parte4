<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>forms get e post</title>
    <link href="./ss.css" rel="stylesheet" type="text/css">
</head>
<body class="body-html">

    <table border="1" class="table-css">
        <thead>

            <th>Nome</th>
            <th>RG</th>
            <th>CPF</th>
            <th>Endereço</th>
            <th>Idade</th>
            <th>Birth</th>
            <th>Estações Favoritas</th>
            <th>Sexo</th>
            <th>Cor Favorita</th>
            <th>Comida Favorita</th>
            <th>Hora que Acorda</th>
            <th>Semana de Férias</th>
            <th>Senha</th>
            <th>Cor que Odeia</th>

        </thead>
        <tbody>

            <td>
                <?php 
                    $nome = $_POST["nome"]; 
                    echo "$nome";
                ?>
            </td>

            <td>
                <?php
                    $rg = $_POST["rg"];
                    echo "$rg";
                ?>
            </td>

            <td>
                <?php
                    $cpf = $_POST["cpf"];
                    echo "$cpf";
                ?>    
            </td>

            <td>
                <?php
                    $end = $_POST["endereco"];
                    echo "$end";
                ?>
            </td>

            <td>
                <?php
                    $idade = $_POST["idade"];
                    echo "$idade";
                ?>
            </td>

            <td>
                <?php
                    $birth = $_POST["nascimento"];
                    echo "$birth";
                ?>
            </td>

            <td>
                <?php
                    $estacoes = $_POST["estacoes"];
                    for($i=0;$i<count($estacoes);$i++){
                        echo "$estacoes[$i]<br>";
                    }
                ?>
            </td>

            <td>
                <?php
                    $sexo = $_POST["sexo"];
                    echo "$sexo";
                ?>
            </td>

            <td>
                <?php
                    $cor = $_POST["cor"];
                    echo "$cor";
                ?>
            </td>

            <td>
                <?php
                    $comida = $_POST["food"];
                    echo "$comida";
                ?>
            </td>

            <td>
                <?php
                    $hora = $_POST["hours"];
                    echo "$hora";
                ?>
            </td>

            <td>
                <?php
                    $semana = $_POST["semana"];
                    echo "$semana";
                ?>
            </td>

            <td>
                <?php
                    $senha = $_POST["senha"];
                    echo "$senha";
                ?>
            </td>

            <td>
                <?php
                    $lesscor = $_POST["lesscor"];
                    echo "$lesscor";
                ?>
            </td>

        </tbody>

    </table>

</body>
</html>
