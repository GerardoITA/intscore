<?php
header('Access-Control-Allow-Origin: http://localhost:5173');
header('Access-Control-Allow-Headers: X-Requested-With');
header('Content-Type: application/json');

$path = realpath(dirname(__FILE__) . '/jsonList');
$jsonListPHP = [];

$files = scandir($path);
foreach ($files as $file) {
    if ($file != "." && $file != "..") {
        array_push($jsonListPHP, $file);
    }
};

echo json_encode($jsonListPHP);
?>