<?php
    $json_string = "{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}";
    echo $json_string . "\n";

    $json = json_decode($json_string);
    echo $json['showpassword'] . "\n";
    echo $json['bgcolor'] . "\n";
?>
