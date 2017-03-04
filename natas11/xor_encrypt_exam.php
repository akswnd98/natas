<?php
    $string = "hello";
    echo 'r, u: ' . ord('r') . ', ' . ord('u') . ': ' . ord('r' ^ 'u') . ' ' . (ord('r') ^ ord('u')) . "\n";
    echo 'g, j: ' . ord('g') . ', ' . ord('j') . ': ' . ord('g' ^ 'j') . ' ' . (ord('g') ^ ord('j')) . "\n";
    echo 'a, b: ' . ord('a') . ', ' . ord('b') . ': ' . ord('a' ^ 'b') . ' ' . (ord('a') ^ ord('b')) . "\n";
?>
