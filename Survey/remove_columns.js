function removeEmptyColumns() {
    $('#mytable tr th').each(function(i) {
      //select all td in this column
      var tds = $(this).parents('table')
        .find(`tr td:nth-child(${i + 1})`);
      // check if all the cells in this column are empty
      // Note: Empty strings return 'false' - trim whitespace before.
      if (tds.toArray().every(td => !td.textContent.trim())) {
        //hide header
        $(this).hide();
        //hide cells
        tds.hide();
      }
    });
  }