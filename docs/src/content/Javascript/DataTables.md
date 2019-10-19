Title: DataTables JS Library
Date: 2018-01-21 00:49
Authors: José Aniceto


[Documentation here](https://datatables.net/manual/index)

### Requirements:
- JQuery

### Usage:
Include the CSS and JS code for DataTables to the head and bottom of the body of your website, respectively. CSS is not required.

```html
<link rel="stylesheet" type="text/css" href= "{{ url_for('static',filename='style.css') }}"> 

<script type="text/javascript" src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js"></script>
```

Use the single function bellow to call to initialise the tabl. Do not forget to add an id tag to the table.
```javascript
$(document).ready(function(){
    $('#myTable').DataTable();
});
```

Add options like so:
```javascript
$(document).ready(function() {
  $('#myTable').DataTable( {
    "columnDefs": [
      { "orderable": false, "targets": [2,3,4] }
    ],
    "paging": false,
    "order": [[ 0, "asc" ]]
  } );
} );
```
