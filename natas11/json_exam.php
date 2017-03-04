<?php
    $data = array("var1" => "hello", "var2" => "nice to meet you");
    $data_string = json_encode($data);
    echo $data_string . "\n";
    $data_php = json_decode($data_string, true);
    foreach($data_php as $key => $value) {
        echo "$key: {$value}\n";
    }
?>

