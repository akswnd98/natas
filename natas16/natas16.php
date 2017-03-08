<?php
    passthru("grep -i \"\$(if [ \$(arr=(\$(cat dict.txt))\nword=\${arr[0]}\necho \${word:0:1}) = h ]\nthen\nsleep 5\nfi)\" dict.txt");
?>
