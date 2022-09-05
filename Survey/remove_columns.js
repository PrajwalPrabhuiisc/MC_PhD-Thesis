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