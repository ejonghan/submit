<?php

if(isset($_POST['submit'])){

$conn = mysqli_connect("localhost", "root", "1005", "tellmeaboutme");

$qury = "INSERT INTO list(writter, description, created) VALUE("Lee", "abcde", NOW());"
mysqli_query($conn, $qury);

header("Location:/submit");
}
?>
