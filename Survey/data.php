<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style.css">
</head>
<body>

<h2>User-Identification Form</h2>
<div class="container">
  <form action="action_page.php"  method="POST" onsubmit="return confirm('Are you sure you want to submit this form?');">
    <div class="row">
      <div class="col-25">
        <label for="fname">First Name</label>
      </div>
      <div class="col-75">
        <input type="text" id="fname" name="firstname" placeholder="Your First name.." required>
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="lname">Last Name</label>
      </div>
      <div class="col-75">
        <input type="text" id="lname" name="lastname" placeholder="Your last name.." required>
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="designation">Designation</label>
      </div>
      <div class="col-75">
        <input type="text" id="lname" name="designation" placeholder="Enter your designation.." required>
      </div>
    </div>
	<div class="row">
      <div class="col-25">
        <label for="email">E-mail</label>
      </div>
      <div class="col-75">
        <input type="text" id="email" name="email" placeholder="abc@xyz.com" required>
      </div>
    </div>
	<div class = "row">
		<div class = "col-25">
		<label for="Human">Select the people you interact with:</label>
		</div>
		<div class="row">
		<label>
     	  <input type="checkbox" checked = "checked" name="person1" value="Vishal Singh" onclick="return false"> Vishal Singh
		  <input type="checkbox" name="person2" value="Vignesh Rana"> Vignesh Rana
		  <input type="checkbox" name="person3" value="Prajwal Prabhu"> Prajwal Prabhu
		  <input type="checkbox" name="person4" value="Uttam Jodawat"> Uttam Jodawat
		  <input type="checkbox" name="person5" value="Naveen Kumar"> Naveen Kumar
		  <input type="checkbox" name="person6" value="Likhinya"> Likhinya
		  <input type="checkbox" name="person7" value="Renu "> Renu 
		  <input type="checkbox" name="person8" value="Divyanshu Bajpai"> Divyanshu Bajpai
    	</label>
		</div>
	</div>
	<div class = "row">
		<div class = "col-25">
		<label for="Software">Select the Software you use:</label>
		</div>
		<div class="row">
		<label>
     	  <input type="checkbox" name="S1" value="Autocad Revit"> Autocad Revit
		  <input type="checkbox" name="S2" value="Arduino"> Arduino
		  <input type="checkbox" checked = "checked" name="S3" value = "Microsoft teams" onclick="return false"> Microsoft teams
		  <input type="checkbox" checked = "checked"name="S4" value = "Outlook" onclick="return false"> Outlook
		  <input type="checkbox" name="S5" value = "Creo"> Creo
		  <input type="checkbox" name="S6" value = "Unity"> Unity
		  <input type="checkbox" name="S7" value = "Python"> Python
		  <input type="checkbox" name="S8" value = "Navisworks"> Navisworks
    	</label>
		</div>
	</div>
	<div class = "row">
		<div class = "col-25">
		<label for="Hardware">Select the Hardware you use</label>
		</div>
		<div class="row">
		<label>
     	  <input type="checkbox" name="H1" value = "NodeMCU(Microcontroller)"> NodeMCU(Microcontroller)
		  <input type="checkbox" name="H2" value = "Raspberry-Pi"> Raspberry-Pi
		  <input type="checkbox" name="H3" value = "Motor Driver"> Motor Driver
		  <input type="checkbox" name="H4" value="Ultrasonic sensor"> Ultrasonic sensor
		  <input type="checkbox" name="H5" value="IR Sensor"> IR Sensor
		  <input type="checkbox" name="H6" value="Wifi-Router">Wifi-Router
    	</label>
		</div>
	</div>
    <div class="row">
      <input type="submit" value="Submit">
    </div>
	<input type="hidden" id="refreshed" value="no">
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
  </form>
</div>
</body>
</html>