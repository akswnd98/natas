<?php
    function xor_encrypt($in, $key) {
        $text = $in;
        $outText = "";

        for($i = 0; $i < strlen($text); $i++) {
            $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }
    
    $key = "qw8J";
    $data = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
    $data = json_encode($data);
    echo $data . "\n";
    $data = xor_encrypt($data, $key);
    $data = base64_encode($data);
    echo $data . "\n";
    echo "\n";

    $data = json_decode(xor_encrypt(base64_decode($data), $key), true);
    echo $data['showpassword'] . "\n" . $data['bgcolor'] . "\n";
?>
