<!DOCTYPE html>
<html>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="mystyle.css">
<script src="remove_columns.js"></script> 
<body onload="removeEmptyColumns()">
<h1><center>Feedback page for Human Interactions</center></h1>
<form action="software.php"  method="POST" onsubmit="return confirm('Are you sure you want to submit this form?');">
<table style="width:100%" id="mytable">
  <tr>
  <th><center>Questions</center></th>
  <th><center><?php echo $_REQUEST['person1'] ?></center></th>
  <th><center><?php if(empty($_REQUEST['person2'])) {
    echo "";
}
else {
    echo $_REQUEST['person2'];
}?></center></th>
  <th><center><?php if(empty($_REQUEST['person3'])) {
    echo "";
    
}
else {
    echo $_REQUEST['person3'];
}?></center></th>
  <th><center><?php if(empty($_REQUEST['person4'])) {
    echo "";
}
else {
    echo $_REQUEST['person4'];
}?></center></th>
  <th><center><?php if(empty($_REQUEST['person5'])) {
    echo "";
}
else {
    echo $_REQUEST['person5'];
}?></center></th>
  <th><center><?php if(empty($_REQUEST['person6'])) {
    echo "";
}
else {
    echo $_REQUEST['person6'];
}?></center></th>
  <th><center><?php if(empty($_REQUEST['person7'])) {
    echo "";
}
else {
    echo $_REQUEST['person7'];
}?></center></th>
  <th><center><?php if(empty($_REQUEST['person8'])) {
    echo "";
}
else {
    echo $_REQUEST['person8'];
}?></center></th>
  </tr>
  <tr>
    <td>1.How often did you plan to have communication with this project member based on the project requirements?</td>
    <td>
     <input type="radio" id="Daily" name="H1" value="1">
     <label for="Daily">Daily</label><br>
     <input type="radio" id="Weekly" name="H1" value="2">
     <label for="Weekly">Weekly</label><br>
     <input type="radio" id="Biweekly" name="H1" value="3">
     <label for="Biweekly">Biweekly</label><br>
     <input type="radio" id="Monthly" name="H1" value="4">
     <label for="Monthly">Monthly</label><br>
     <input type="radio" id="Bimonthly" name="H1" value="5">
     <label for="Bimonthly">Bimonthly</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
     echo '<input type="radio" name="H2" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
     echo '<label for="Daily">Daily</label><br>';
     echo '<input type="radio" id="Weekly" name="H2" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
     echo '<label for="Weekly">Weekly</label><br>';
     echo '<input type="radio" id="Biweekly" name="H2" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
     echo '<label for="Biweekly">Biweekly</label><br>';
     echo '<input type="radio" id="Monthly" name="H2" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
     echo '<label for="Monthly">Monthly</label><br>';
     echo '<input type="radio" id="Bimonthly" name="H2" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
     echo'<label for="Bimonthly">Bimonthly</label><br>';
}?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";   
    }
    else {
      echo '<input type="radio" name="H3" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H3" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H3" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H3" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H3" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }?>
    </td>
    
    <td>
    <?php if(empty($_REQUEST['person4'])) {
      echo "";
    }
      else {
        echo '<input type="radio" name="H4" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
        echo '<label for="Daily">Daily</label><br>';
        echo '<input type="radio" id="Weekly" name="H4" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
        echo '<label for="Weekly">Weekly</label><br>';
        echo '<input type="radio" id="Biweekly" name="H4" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
        echo '<label for="Biweekly">Biweekly</label><br>';
        echo '<input type="radio" id="Monthly" name="H4" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
        echo '<label for="Monthly">Monthly</label><br>';
        echo '<input type="radio" id="Bimonthly" name="H4" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
        echo'<label for="Bimonthly">Bimonthly</label><br>';
      }?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
           echo "";
          }
          else {
            echo '<input type="radio" name="H5" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
            echo '<label for="Daily">Daily</label><br>';
            echo '<input type="radio" id="Weekly" name="H5" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
            echo '<label for="Weekly">Weekly</label><br>';
            echo '<input type="radio" id="Biweekly" name="H5" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
            echo '<label for="Biweekly">Biweekly</label><br>';
            echo '<input type="radio" id="Monthly" name="H5" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
            echo '<label for="Monthly">Monthly</label><br>';
            echo '<input type="radio" id="Bimonthly" name="H5" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
            echo'<label for="Bimonthly">Bimonthly</label><br>';
        }?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
           echo "";
        }
          else {
            echo '<input type="radio" name="H6" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
            echo '<label for="Daily">Daily</label><br>';
            echo '<input type="radio" id="Weekly" name="H6" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
            echo '<label for="Weekly">Weekly</label><br>';
            echo '<input type="radio" id="Biweekly" name="H6" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
            echo '<label for="Biweekly">Biweekly</label><br>';
            echo '<input type="radio" id="Monthly" name="H6" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
            echo '<label for="Monthly">Monthly</label><br>';
            echo '<input type="radio" id="Bimonthly" name="H6" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
            echo'<label for="Bimonthly">Bimonthly</label><br>';
        }?>
    </td>
    
    <td>
        <?php if(empty($_REQUEST['person7'])) {
            echo "";
            }
          else {
            echo '<input type="radio" name="H7" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
            echo '<label for="Daily">Daily</label><br>';
            echo '<input type="radio" id="Weekly" name="H7" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
            echo '<label for="Weekly">Weekly</label><br>';
            echo '<input type="radio" id="Biweekly" name="H7" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
            echo '<label for="Biweekly">Biweekly</label><br>';
            echo '<input type="radio" id="Monthly" name="H7" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
            echo '<label for="Monthly">Monthly</label><br>';
            echo '<input type="radio" id="Bimonthly" name="H7" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
            echo'<label for="Bimonthly">Bimonthly</label><br>';
          }?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
            echo "";
            }
          else {
            echo '<input type="radio" name="H8" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
            echo '<label for="Daily">Daily</label><br>';
            echo '<input type="radio" id="Weekly" name="H8" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
            echo '<label for="Weekly">Weekly</label><br>';
            echo '<input type="radio" id="Biweekly" name="H8" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
            echo '<label for="Biweekly">Biweekly</label><br>';
            echo '<input type="radio" id="Monthly" name="H8" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
            echo '<label for="Monthly">Monthly</label><br>';
            echo '<input type="radio" id="Bimonthly" name="H8" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
            echo'<label for="Bimonthly">Bimonthly</label><br>';
          }?>
    </td>
  </tr>
  <tr>
    <td>1a.How often do you actually communicate with this project member?</td>
    <td>
     <input type="radio" id="Daily" name="H9" value="1">
     <label for="Daily">Daily</label><br>
     <input type="radio" id="Weekly" name="H9" value="2">
     <label for="Weekly">Weekly</label><br>
     <input type="radio" id="Biweekly" name="H9" value="3">
     <label for="Biweekly">Biweekly</label><br>
     <input type="radio" id="Monthly" name="H9" value="4">
     <label for="Monthly">Monthly</label><br>
     <input type="radio" id="Bimonthly" name="H9" value="5">
     <label for="Bimonthly">Bimonthly</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H10" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H10" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H10" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H10" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H10" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>
    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H11" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H11" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H11" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H11" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H11" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H12" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H12" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H12" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H12" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H12" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H13" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H13" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H13" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H13" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H13" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H14" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H14" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H14" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H14" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H14" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H15" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H15" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H15" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H15" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H15" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H16" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H16" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H16" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H16" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H16" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>
  </tr>
  <tr>
    <td>2.How easy did you expect it would be to be able to access this project member based on the need?</td>
    <td>
     <input type="radio" id="H17" name="H17" value="1">
     <label for="Daily">Very easy</label><br>
     <input type="radio" id="H17" name="H17" value="2">
     <label for="Weekly">Easy</label><br>
     <input type="radio" id="H17" name="H17" value="3">
     <label for="Biweekly">Neither easy nor &nbsp;&nbsp;difficult</label><br>
     <input type="radio" id="H17" name="H17" value="4">
     <label for="Monthly">Difficult</label><br>
     <input type="radio" id="H17" name="H17" value="5">
     <label for="Bimonthly">Very difficult</label><br>
    </td>


    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H18" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H18" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H18" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H18" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H18" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>
    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H19" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H19" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H19" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H19" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H19" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>
  
    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H20" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H20" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H20" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H20" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H20" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H21" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H21" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H21" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H21" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H21" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H22" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H22" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H22" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H22" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H22" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H23" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H23" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H23" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H23" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H23" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H24" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H24" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H24" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H24" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H24" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

  </tr>

  <tr>
    <td>2a. How easy has it actually been to access this project member when needed?</td>
    <td>
     <input type="radio" id="H25" name="H25" value="1">
     <label for="Daily">Very easy</label><br>
     <input type="radio" id="H25" name="H25" value="2">
     <label for="Weekly">Easy</label><br>
     <input type="radio" id="H25" name="H25" value="3">
     <label for="Biweekly">Neither easy nor &nbsp;&nbsp;&nbsp;&nbsp;difficult</label><br>
     <input type="radio" id="H25" name="H25" value="4">
     <label for="Monthly">Difficult</label><br>
     <input type="radio" id="H25" name="H25" value="5">
     <label for="Bimonthly">Very difficult</label><br>
    </td>



    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H26" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H26" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H26" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H26" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H26" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H27" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H27" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H27" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H27" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H27" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H28" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H28" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H28" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H28" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H28" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H29" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H29" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H29" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H29" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H29" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H30" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H30" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H30" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H30" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H30" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H31" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H31" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H31" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H31" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H31" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H32" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very easy</label><br>';
      echo '<input type="radio" id="Weekly" name="H32" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Easy</label><br>';
      echo '<input type="radio" id="Biweekly" name="H32" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neither easy nor difficult</label><br>';
      echo '<input type="radio" id="Monthly" name="H32" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Difficult</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H32" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very difficult</label><br>';
    }
    ?>
    </td>

  </tr>

  <tr>
    <td>3. As per the project plan, how well-defined were the roles and responsibilities of this project member?</td>
    <td>
     <input type="radio" id="H33" name="H33" value="1">
     <label for="Daily">Excellently defined</label><br>
     <input type="radio" id="H33" name="H33" value="2">
     <label for="Weekly">Reasonably defined</label><br>
     <input type="radio" id="H33" name="H33" value="3">
     <label for="Biweekly">Neutral</label><br>
     <input type="radio" id="H33" name="H33" value="4">
     <label for="Monthly">Not well defined</label><br>
     <input type="radio" id="H33" name="H33" value="5">
     <label for="Bimonthly">Poorly defined</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H34" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H34" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H34" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H34" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H34" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H35" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H35" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H35" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H35" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H35" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H36" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H36" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H36" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H36" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H36" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H37" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H37" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H37" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H37" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H37" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H38" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H38" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H38" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H38" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H38" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H39" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H39" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H39" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H39" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H39" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H40" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H40" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H40" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H40" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H40" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

  </tr>

  <td>3a. How well is this project member performing in the roles and responsibilities defined for them?</td>
    <td>
     <input type="radio" id="H41" name="H41" value="1">
     <label for="Daily">Excellently defined</label><br>
     <input type="radio" id="H41" name="H41" value="2">
     <label for="Weekly">Reasonably defined</label><br>
     <input type="radio" id="H41" name="H41" value="3">
     <label for="Biweekly">Neutral</label><br>
     <input type="radio" id="H41" name="H41" value="4">
     <label for="Monthly">Not well defined</label><br>
     <input type="radio" id="H41" name="H41" value="5">
     <label for="Bimonthly">Poorly defined</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H42" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H42" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H42" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H42" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H42" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H43" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H43" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H43" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H43" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H43" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H44" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H44" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H44" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H44" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H44" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H45" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H45" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H45" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H45" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H45" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H46" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H46" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H46" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H46" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H46" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H47" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H47" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H47" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H47" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H47" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H48" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Excellently defined</label><br>';
      echo '<input type="radio" id="Weekly" name="H48" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Reasonably defined</label><br>';
      echo '<input type="radio" id="Biweekly" name="H48" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H48" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Not well defined</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H48" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Poorly defined</label><br>';
    }
    ?>
    </td>

  </tr>

  <tr>
    <td>4.To what extent the information exchanged with the project member has to be error-free /Trustable?</td>
    <td>
     <input type="radio" id="H49" name="H49" value="1">
     <label for="Daily">Not important</label><br>
     <input type="radio" id="H49" name="H49" value="2">
     <label for="Weekly">Some error is fine</label><br>
     <input type="radio" id="H49" name="H49" value="3">
     <label for="Biweekly">Neutral</label><br>
     <input type="radio" id="H49" name="H49" value="4">
     <label for="Monthly">Important</label><br>
     <input type="radio" id="H49" name="H49" value="5">
     <label for="Bimonthly">Very important</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H50" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H50" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H50" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H50" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H50" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H51" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H51" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H51" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H51" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H51" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H52" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H52" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H52" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H52" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H52" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H53" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H53" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H53" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H53" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H53" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H54" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H54" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H54" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H54" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H54" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H55" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H55" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H55" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H55" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H55" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H56" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H56" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Some error is fine</label><br>';
      echo '<input type="radio" id="Biweekly" name="H56" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H56" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Important</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H56" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very important</label><br>';
    }
    ?>
    </td>

  </tr>
  
  <td>4a. How much do you actually trust the information exchanged by the project member?</td>
    <td>
     <input type="radio" id="H57" name="H57" value="1">
     <label for="Daily">Not important</label><br>
     <input type="radio" id="H57" name="H57" value="2">
     <label for="Weekly">Somewhat</label><br>
     <input type="radio" id="H57" name="H57" value="3">
     <label for="Biweekly">Neutral</label><br>
     <input type="radio" id="H57" name="H57" value="4">
     <label for="Monthly">High</label><br>
     <input type="radio" id="H57" name="H57" value="5">
     <label for="Bimonthly">Completely</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H58" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H58" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H58" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H58" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H58" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H59" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H59" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H59" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H59" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H59" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H60" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H60" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H60" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H60" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H60" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H61" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H61" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H61" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H61" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H61" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H62" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H62" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H62" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H62" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H62" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H63" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H63" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H63" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H63" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H63" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H64" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Not important</label><br>';
      echo '<input type="radio" id="Weekly" name="H64" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Somewhat</label><br>';
      echo '<input type="radio" id="Biweekly" name="H64" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Neutral</label><br>';
      echo '<input type="radio" id="Monthly" name="H64" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">High</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H64" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Completely</label><br>';
    }
    ?>
    </td>

  </tr>

  <tr>
    <td>5.To what extent did you expect or you were expected to enhance this project member's capabilities by training or sharing knowledge?</td>
    <td>
     <input type="radio" id="H65" name="H65" value="1">
     <label for="Daily">Very rarely</label><br>
     <input type="radio" id="H65" name="H65" value="2">
     <label for="Weekly">Rarely</label><br>
     <input type="radio" id="H65" name="H65" value="3">
     <label for="Biweekly">Occasionally</label><br>
     <input type="radio" id="H65" name="H65" value="4">
     <label for="Monthly">Regularly</label><br>
     <input type="radio" id="H65" name="H65" value="5">
     <label for="Bimonthly">Very regularly</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H66" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H66" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H66" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H66" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H66" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H67" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H67" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H67" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H67" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H67" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H68" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H68" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H68" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H68" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H68" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H69" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H69" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H69" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H69" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H69" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H70" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H70" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H70" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H70" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H70" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H71" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H71" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H71" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H71" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H71" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H72" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H72" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H72" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H72" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H72" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

  </tr>

  <td>5a. To what extent do you actually share relevant information or knowledge with the project member to enhance their primary
expertise?</td>
    <td>
	<input type="radio" id="H73" name="H73" value="1">
     <label for="Daily">Very rarely</label><br>
     <input type="radio" id="H73" name="H73" value="2">
     <label for="Weekly">Rarely</label><br>
     <input type="radio" id="H73" name="H73" value="3">
     <label for="Biweekly">Occasionally</label><br>
     <input type="radio" id="H73" name="H73" value="4">
     <label for="Monthly">Regularly</label><br>
     <input type="radio" id="H73" name="H73" value="5">
     <label for="Bimonthly">Very regularly</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H74" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H74" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H74" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H74" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H74" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H75" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H75" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H75" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H75" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H75" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H76" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H76" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H76" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H76" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H76" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H77" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H77" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H77" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H77" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H77" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H78" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H78" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H78" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H78" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H78" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H79" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H79" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H79" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H79" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H79" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H80" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Very rarely</label><br>';
      echo '<input type="radio" id="Weekly" name="H80" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Rarely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H80" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Occasionally</label><br>';
      echo '<input type="radio" id="Monthly" name="H80" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Regularly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H80" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Very regularly</label><br>';
    }
    ?>
    </td>

  </tr>
  
  
  <td>6. Is there any planned activity in the project to inform you about this person's new duties, job changes, job status and
responsibilities?</td>
    <td>
     <input type="radio" id="H81" name="H81" value="1">
     <label for="Daily">Daily</label><br>
     <input type="radio" id="Weekly" name="H81" value="2">
     <label for="Weekly">Weekly</label><br>
     <input type="radio" id="Biweekly" name="H81" value="3">
     <label for="Biweekly">Biweekly</label><br>
     <input type="radio" id="Monthly" name="H81" value="4">
     <label for="Monthly">Monthly</label><br>
     <input type="radio" id="Bimonthly" name="H81" value="5">
     <label for="Bimonthly">Bimonthly</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H82" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H82" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H82" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H82" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H82" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H83" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H83" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H83" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H83" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H83" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H84" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H84" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H84" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H84" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H84" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H85" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H85" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H85" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H85" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H85" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H86" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H86" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H86" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H86" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H86" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H87" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H87" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H87" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H87" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H87" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H88" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H88" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H88" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H88" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H88" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

  </tr>

  <td>6a. How updated are you about the changes and status of project member's tasks, responsibilities and current level of skills?</td>
    <td>
    <input type="radio" id="Daily" name="H89" value="1">
     <label for="Daily">Daily</label><br>
     <input type="radio" id="Weekly" name="H89" value="2">
     <label for="Weekly">Weekly</label><br>
     <input type="radio" id="Biweekly" name="H89" value="3">
     <label for="Biweekly">Biweekly</label><br>
     <input type="radio" id="Monthly" name="H89" value="4">
     <label for="Monthly">Monthly</label><br>
     <input type="radio" id="Bimonthly" name="H89" value="5">
     <label for="Bimonthly">Bimonthly</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H90" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H90" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H90" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H90" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H90" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H91" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H91" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H91" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H91" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H91" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H92" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H92" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H92" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H92" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H92" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H93" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H93" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H93" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H93" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H93" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H94" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H94" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H94" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H94" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H94" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H95" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H95" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H95" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H95" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H95" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H96" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Daily</label><br>';
      echo '<input type="radio" id="Weekly" name="H96" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Weekly</label><br>';
      echo '<input type="radio" id="Biweekly" name="H96" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Biweekly</label><br>';
      echo '<input type="radio" id="Monthly" name="H96" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Monthly</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H96" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">Bimonthly</label><br>';
    }
    ?>
    </td>

  </tr>

    <td>7. Is there any plan to assist project members to know how to retrieve needed information from whom?</td>
    <td>
     <input type="radio" id="Daily" name="H97" value="1">
     <label for="Daily">Yes</label><br>
     <input type="radio" id="Weekly" name="H97" value="2">
     <label for="Weekly">Likely</label><br>
     <input type="radio" id="Biweekly" name="H97" value="3">
     <label for="Biweekly">Not sure</label><br>
     <input type="radio" id="Monthly" name="H97" value="4">
     <label for="Monthly">Unlikely</label><br>
     <input type="radio" id="Bimonthly" name="H97" value="5">
     <label for="Bimonthly">No</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H98" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H98" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H98" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H98" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H98" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H99" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H99" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H99" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H99" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H99" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H100" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H100" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H100" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H100" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H100" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H101" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H101" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H101" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H101" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H101" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H102" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H102" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H102" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H102" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H102" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H103" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H103" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H103" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H103" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H103" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H104" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H104" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H104" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H104" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H104" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

  </tr>

    <tr>
    <td>7a. Has it been easy for this project member to know who to contact for what, and how to contact them (find contact information of people relevant to the project)?</td>
    <td>
    <input type="radio" id="Daily" name="H105" value="1">
     <label for="Daily">Yes</label><br>
     <input type="radio" id="Weekly" name="H105" value="2">
     <label for="Weekly">Likely</label><br>
     <input type="radio" id="Biweekly" name="H105" value="3">
     <label for="Biweekly">Not sure</label><br>
     <input type="radio" id="Monthly" name="H105" value="4">
     <label for="Monthly">Unlikely</label><br>
     <input type="radio" id="Bimonthly" name="H105" value="5">
     <label for="Bimonthly">No</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H106" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H106" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H106" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H106" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H106" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H107" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H107" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H107" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H107" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H107" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H108" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H108" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H108" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H108" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H108" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H109" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H109" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H109" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H109" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H109" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H110" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H110" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H110" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H110" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H110" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H111" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H111" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H111" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H111" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H111" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H112" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">Yes</label><br>';
      echo '<input type="radio" id="Weekly" name="H112" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Likely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H112" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Not sure</label><br>';
      echo '<input type="radio" id="Monthly" name="H112" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Unlikely</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H112" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">No</label><br>';
    }
    ?>
    </td>

  </tr>

    <tr>
    <td>8. Is there any substitute source for the information or knowledge coming from the project member in case the member leaves the project?</td>
    <td>
    <input type="radio" id="Daily" name="H113" value="1">
     <label for="Daily">No</label><br>
     <input type="radio" id="Weekly" name="H113" value="2">
     <label for="Weekly">Unlikely</label><br>
     <input type="radio" id="Biweekly" name="H113" value="3">
     <label for="Biweekly">Likely</label><br>
     <input type="radio" id="Monthly" name="H113" value="4">
     <label for="Monthly">Yes</label><br>
     <input type="radio" id="Bimonthly" name="H113" value="5">
     <label for="Bimonthly">I do not know</label><br>
    </td>

    <td>
    <?php if(empty($_REQUEST['person2'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H114" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H114" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H114" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H114" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H114" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person3'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H115" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H115" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H115" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H115" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H115" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person4'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H116" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H116" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H116" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H116" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H116" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person5'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H117" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H117" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H117" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H117" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H117" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person6'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H118" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H118" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H118" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H118" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H118" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person7'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H119" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H119" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H119" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H119" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H119" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    <td>
    <?php if(empty($_REQUEST['person8'])) {
    echo "";
    }
    else {
      echo '<input type="radio" name="H120" value="1"'.htmlspecialchars(1, ENT_QUOTES).'">';
      echo '<label for="Daily">No</label><br>';
      echo '<input type="radio" id="Weekly" name="H120" value="2"'.htmlspecialchars(2, ENT_QUOTES).'">';
      echo '<label for="Weekly">Unlikely</label><br>';
      echo '<input type="radio" id="Biweekly" name="H120" value="3"'.htmlspecialchars(3, ENT_QUOTES).'">';
      echo '<label for="Biweekly">Likely</label><br>';
      echo '<input type="radio" id="Monthly" name="H120" value="4"'.htmlspecialchars(4, ENT_QUOTES).'">';
      echo '<label for="Monthly">Yes</label><br>';
      echo '<input type="radio" id="Bimonthly" name="H120" value="5"'.htmlspecialchars(5, ENT_QUOTES).'">';
      echo'<label for="Bimonthly">I do not know</label><br>';
    }
    ?>
    </td>

    </tr>

  </tr>
</table>
</div>
<div>
<input type="submit" value="Submit">
</div>
</form>
		<?php
		error_reporting(0);
		echo "<script type='text/javascript'>
    function clicked() {
       if (confirm('Do you want to submit?')) {
           yourformelement.submit();
       } else {
           return false;
       }
    } 

</script>";
		// servername => localhost
		// username => root
		// password => empty
		// database name => staff
		$conn = mysqli_connect("localhost", "root", "", "survey");
		
		// Check connection
		if($conn === false){
			die("ERROR: Could not connect. "
				. mysqli_connect_error());
		}
		
		// Taking all 5 values from the form data(input)
		$firstname = $_REQUEST['firstname'];
		$lastname = $_REQUEST['lastname'];
		$designation = $_REQUEST['designation'];
		$emailid = $_REQUEST['email'];
		$Human1 = $_REQUEST['person1'];
        $Human2 = $_REQUEST['person2'];
        $Human3 = $_REQUEST['person3'];
        $Human4 = $_REQUEST['person4'];
        $Human5 = $_REQUEST['person5'];
        $Human6 = $_REQUEST['person6'];
        $Human7 = $_REQUEST['person7'];
        $Human8 = $_REQUEST['person8'];
        $S1 = $_REQUEST['S1'];
        $S2 = $_REQUEST['S2'];
        $S3 = $_REQUEST['S3'];
        $S4 = $_REQUEST['S4'];
        $S5 = $_REQUEST['S5'];
        $S6 = $_REQUEST['S6'];
        $S7 = $_REQUEST['S7'];
        $S8 = $_REQUEST['S8'];
        $H1 = $_REQUEST['H1'];
        $H2 = $_REQUEST['H2'];
        $H3 = $_REQUEST['H3'];
        $H4 = $_REQUEST['H4'];
        $H5 = $_REQUEST['H5'];
        $H6 = $_REQUEST['H6'];
		
		// Performing insert query execution
		// here our table name is college
		$sql = "INSERT INTO users VALUES ('$firstname',
			'$lastname','$designation','$emailid','$Human1','$Human2','$Human3','$Human4','$Human5','$Human6','$Human7','$Human8',
            '$S1','$S2','$S3','$S4','$S5','$S6','$S7','$S8','$H1','$H2','$H3','$H4','$H5','$H6')";
		$message = 'Data has been submitted successfully!';
		if(mysqli_query($conn, $sql)){
			echo "<script type='text/javascript'>alert('$message');</script>";
		} else{
			echo "ERROR: Hush! Sorry $sql. "
				. mysqli_error($conn);
		}
		
		// Close connection
		mysqli_close($conn);
		
		?>
</body>

</html>
