<?php
    function xor_encrypt($in, $key) {
        $text = $in;
        $outText = "";

        for($i = 0; $i < strlen($text); $i++) {
            $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }

    $default = array("showpassword" => "no", "bgcolor" => "#ffffff");
    $default_encrypt = json_encode($default);
    $data_base_decoded = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");

    $key_long = xor_encrypt($default_encrypt, $data_base_decoded);
    echo $key_long . "\n";

    $key = "";
    for($i = 0; $i < 4; $i++) {
        $key .= $key_long[$i];
    }

    echo $key . "\n";

    $usedata = array("showpassword" => "yes", "bgcolor" => "#ffffff");
    $usedata = json_encode($usedata);
    $usedata = xor_encrypt($key, $usedata);
    $usedata = base64_encode($usedata);

    echo $usedata;
?>
