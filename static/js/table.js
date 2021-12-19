$(document).ready(function() {
    $('#product_table').dataTable( {
        // Sets the row-num-selection "Show %n entries" for the user
        "lengthMenu": [ 20, 40, 60, 80, 100 ],

        // Set the default no. of rows to display
        "pageLength": 10
         responsive: true
    } );
} );


$(document).ready(function() {
    $('#example').dataTable( {
        // Sets the row-num-selection "Show %n entries" for the user
        "lengthMenu": [ 20, 40, 60, 80, 100 ],

        // Set the default no. of rows to display
        "pageLength": 20
    } );
} );