<?php
$servername = "localhost";
$username = "root";
$password = "atul";
$database = "atul";
$conn = mysqli_connect($servername, $username, $password,
$database);
$name = "atul";
$rollNO= 29;
$college="jit";
$branch="cse";
$sql = "INSERT INTO `students` (`name`,
`rollNO`,'college','branch') VALUES ('$name',
'$rollNO','$college','$branch')";
$result = mysqli_query($conn, $sql);
?>
