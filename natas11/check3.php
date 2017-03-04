<?php
    $data = array("showpassword" => "no", "bgcolor" => "#ffffff");
    $json_string = json_encode($data);
    echo $json_string . "\n";
    
    $json = json_decode($json_string, true);
    echo $json['showpassword'] . "\n";
    echo $json['bgcolor'] . "\n";
?>
