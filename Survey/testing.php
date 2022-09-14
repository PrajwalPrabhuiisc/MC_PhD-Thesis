<!DOCTYPE html>
<html>
<body>

<?php  
for ($x = 0; $x <= 10; $x++) {
  echo "H$x = person$x <br>";
}
?>  

</body>
<input type="hidden" id="refreshed" value="no">
    <script type="text/javascript">

           onload=function(){
               var e=document.getElementById("refreshed");
               if(e.value=="no")e.value="yes";
               else{e.value="no";location.reload();}
           }

    </script>
</html>
