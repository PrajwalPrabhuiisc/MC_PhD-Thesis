<!DOCTYPE html>
<html>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>HTML Table</h2>

<table id="mytable">
<tr>
    <th>Company</th>
    <th>name</th>
    <th>Country</th>
    <th>name</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td></td>
    <td>Germany</td>
    <td></td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td></td>
    <td>Mexico</td>
    <td></td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td></td>
    <td>Austria</td>
    <td></td>
    <td>Austria</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td></td>
    <td>UK</td>
    <td></td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td></td>
    <td>Canada</td>
    <td></td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td></td>
    <td>Italy</td>
    <td></td>
    <td>Italy</td>
  </tr>
</table>
<button onclick="removeEmptyColumns()">Remove empty columns</button>
<script>
function removeEmptyColumns() {
  $('#mytable tr th').each(function(i) {
     //select all tds in this column
     var tds = $(this).parents('table')
              .find('tr td:nth-child(' + (i + 1) + ')');
        //check if all the cells in this column are empty
        if(tds.length == tds.filter(':empty').length) { 
            //hide header
            $(this).hide();
            //hide cells
            tds.hide();
        } 
}); 
}
</script>
</body>
</html>

