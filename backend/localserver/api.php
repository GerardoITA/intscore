<?php
header('Access-Control-Allow-Origin: http://localhost:5173');
header('Access-Control-Allow-Headers: X-Requested-With');
header('Content-Type: application/json');

/* include_once './pathJson.php';  // Include il file che restituisce l'array di json */
$path = realpath(dirname(__FILE__) . '/jsonList');
$jsonListPHP = [];
$files = scandir($path);
foreach ($files as $file) {
    if ($file != "." && $file != "..") {
        array_push($jsonListPHP, $file);
    }
}
;

$arrayJson = []; // Creo un array vuoto per contenere i json
foreach($jsonListPHP as $json) {
    $jsonContent = file_get_contents($path . '/' . $json); // Prende il contenuto del file cercandolo nel path costruito con $path + nome del json
    $jsonDecoded = json_decode($jsonContent, true); // Decodifica il contenuto del file
    $jsonName = pathinfo($json, PATHINFO_FILENAME);
    $arrayJson[$jsonName . ".json"] = $jsonDecoded; // Aggiunge il contenuto del json di cui sopra all'array e usa come key il nome del file
   /*  array_push($arrayJson, $jsonDecoded); ; // Aggiunge il contenuto del json sopra all'array */

};
$arrayEncoded = json_encode($arrayJson);
echo $arrayEncoded;
?>