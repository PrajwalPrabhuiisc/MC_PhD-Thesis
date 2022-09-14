<?php
error_reporting(0);
$conn = mysqli_connect("localhost", "root", "", "survey");
// Check connection
if($conn === false){
    die("ERROR: Could not connect. "
        . mysqli_connect_error());
}
$H1	= $_REQUEST['H1'];$H2= $_REQUEST['H2'];$H3	= $_REQUEST['H3'];$H4	= $_REQUEST['H4']; $H5	= $_REQUEST['H5']; $H6	= $_REQUEST['H6']; $H7	= $_REQUEST['H7'];
$H8	= $_REQUEST['H8'];$H9	= $_REQUEST['H9']; $H10= $_REQUEST['H10'];$H11	= $_REQUEST['H11'];$H12	= $_REQUEST['H12']; $H13= $_REQUEST['H13']; $H14= $_REQUEST['H14']; $H15= $_REQUEST['H15'];
$H16= $_REQUEST['H16'];$H17	= $_REQUEST['H17'];$H18	= $_REQUEST['H18']; $H19= $_REQUEST['H19'];$H20	= $_REQUEST['H20'];$H21	= $_REQUEST['H21'];
$H22= $_REQUEST['H22']; $H23= $_REQUEST['H23']; $H24= $_REQUEST['H24'];$H25	= $_REQUEST['H25'];$H26	= $_REQUEST['H26'];$H27	= $_REQUEST['H27'];$H28	= $_REQUEST['H28'];
$H29= $_REQUEST['H29'];$H30= $_REQUEST['H30'];
$H30= $_REQUEST['H30'];$H31= $_REQUEST['H31'];$H32= $_REQUEST['H32'];$H33= $_REQUEST['H33'];$H34= $_REQUEST['H34'];$H35= $_REQUEST['H35'];$H36= $_REQUEST['H36'];$H37= $_REQUEST['H37'];$H38= $_REQUEST['H38'];$H39= $_REQUEST['H39'];$H40= $_REQUEST['H40'];$H41= $_REQUEST['H41'];$H42= $_REQUEST['H42'];$H43= $_REQUEST['H43'];
$H44= $_REQUEST['H44'];$H45= $_REQUEST['H45'];$H46= $_REQUEST['H46'];$H47= $_REQUEST['H47'];$H48= $_REQUEST['H48'];$H49= $_REQUEST['H49'];$H50= $_REQUEST['H50'];$H51= $_REQUEST['H51'];$H52= $_REQUEST['H52'];$H53= $_REQUEST['H53'];$H54= $_REQUEST['H54'];$H55= $_REQUEST['H55'];$H56= $_REQUEST['H56'];$H57= $_REQUEST['H57'];
$H58= $_REQUEST['H58'];$H59= $_REQUEST['H59'];$H60= $_REQUEST['H60'];$H61= $_REQUEST['H61'];$H62= $_REQUEST['H62'];$H63= $_REQUEST['H63'];$H64= $_REQUEST['H64'];$H65= $_REQUEST['H65'];$H66= $_REQUEST['H66'];$H67= $_REQUEST['H67'];$H68= $_REQUEST['H68'];$H69= $_REQUEST['H69'];$H70= $_REQUEST['H70'];$H71= $_REQUEST['H71'];
$H72= $_REQUEST['H72'];$H73= $_REQUEST['H73'];$H74= $_REQUEST['H74'];$H75= $_REQUEST['H75'];$H76= $_REQUEST['H76'];$H77= $_REQUEST['H77'];$H78= $_REQUEST['H78'];$H79= $_REQUEST['H79'];$H80= $_REQUEST['H80'];$H81= $_REQUEST['H81'];$H82= $_REQUEST['H82'];$H83= $_REQUEST['H83'];$H84= $_REQUEST['H84'];$H85= $_REQUEST['H85'];
$H86= $_REQUEST['H86'];$H87= $_REQUEST['H87'];$H88= $_REQUEST['H88'];$H89= $_REQUEST['H89'];$H90= $_REQUEST['H90'];$H91= $_REQUEST['H91'];$H92= $_REQUEST['H92'];$H93= $_REQUEST['H93'];$H94= $_REQUEST['H94'];$H95= $_REQUEST['H95'];$H96= $_REQUEST['H96'];$H97= $_REQUEST['H97'];$H98= $_REQUEST['H98'];$H99= $_REQUEST['H99'];
$H100= $_REQUEST['H100'];$H101= $_REQUEST['H101'];$H102= $_REQUEST['H102'];$H103= $_REQUEST['H103'];$H104= $_REQUEST['H104'];$H105= $_REQUEST['H105'];$H106= $_REQUEST['H106'];$H107= $_REQUEST['H107'];$H108= $_REQUEST['H108'];$H109= $_REQUEST['H109'];$H110= $_REQUEST['H110'];$H111= $_REQUEST['H111'];$H112= $_REQUEST['H112'];$H113= $_REQUEST['H113'];
$H114= $_REQUEST['H114'];$H115= $_REQUEST['H115'];$H116= $_REQUEST['H116'];$H117= $_REQUEST['H117'];$H119= $_REQUEST['H104'];$H120= $_REQUEST['H120'];

$sql1 = "INSERT INTO human1 VALUES ('$H1','$H2','$H3','$H4','$H5','$H6','$H7','$H8','$H9','$H10','$H11','$H12','$H13','$H14','$H15','$H16','$H17','$H18','$H19','$H20','$H21','$H22','$H23','$H24','$H25','$H26','$H27','$H28','$H29','$H30')";
$sql2 = "INSERT INTO human2 VALUES ('$H31','$H32','$H33','$H34','$H35','$H36','$H37','$H38','$H39','$H40','$H41','$H42','$H43','$H44','$H45','$H46','$H47','$H48','$H49','$H50','$H51','$H52','$H53','$H54','$H55','$H56','$H57','$H58','$H59','$H60')";
$sql3 = "INSERT INTO human3 VALUES ('$H61','$H62','$H63','$H64','$H65','$H66','$H67','$H68','$H69','$H70','$H71','$H72','$H73','$H74','$H75','$H76','$H77','$H78','$H79','$H80','$H81','$H82','$H83','$H84','$H85','$H86','$H87','$H88','$H89','$H90')";
$sql4 = "INSERT INTO human4 VALUES ('$H91','$H92','$H93','$H94','$H95','$H96','$H97','$H98','$H99','$H100','$H101','$H102','$H103','$H104','$H105','$H106','$H107','$H108','$H109','$H110','$H111','$H112','$H113','$H114','$H115','$H116','$H117','$H118','$H119','$H120')";

$message = 'Data has been submitted successfully!';

if(mysqli_query($conn, $sql1) and  mysqli_query($conn, $sql2) and mysqli_query($conn, $sql3) and  mysqli_query($conn, $sql4)){
    echo "<script type='text/javascript'>alert('$message');</script>";
} else{
    echo "ERROR: Hush! Sorry $sql. "
        . mysqli_error($conn);
}

// Close connection
mysqli_close($conn);

?>