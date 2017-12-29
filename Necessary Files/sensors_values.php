<?php 

DEFINE ('DBUSER', 'iwagroupa'); 
DEFINE ('DBPW', 'iwagroupa'); 
DEFINE ('DBHOST', 'insightworkshop.cqxmg1hzjwc5.us-west-2.rds.amazonaws.com'); 
DEFINE ('DBNAME', 'iwagroupa'); 

$dbc = mysqli_connect(DBHOST,DBUSER,DBPW);
if (!$dbc) {
    die("Database connection failed: " . mysqli_error($dbc));
    exit();
}

$dbs = mysqli_select_db($dbc, DBNAME);
if (!$dbs) {
    die("Database selection failed: " . mysqli_error($dbc));
    exit(); 
}

$moisture = mysqli_real_escape_string($dbc, $_GET['moisture']);
$pH = mysqli_real_escape_string($dbc,$_GET['pH']);
$humidity = mysqli_real_escape_string($dbc,$_GET['humidity']);
$temperature = mysqli_real_escape_string($dbc,$_GET['temperature']);
$datetime = mysqli_real_escape_string($dbc,$_GET['datetime']);

$query = "INSERT INTO sensors_values (moisture, pH, humidity, temperature, datetime) VALUES ('$moisture', '$pH', '$humidity', '$temperature', '$datetime')";

$result = mysqli_query($dbc, $query) or trigger_error("Query MySQL Error: " . mysqli_error($dbc)); 

mysqli_close($dbc); 

?>
