$(document).ready(function() {
    $('#example').dataTable( {
        // Sets the row-num-selection "Show %n entries" for the user
        "lengthMenu": [ 20, 30 ],

        // Set the default no. of rows to display
        "pageLength": 20,
        'responsive': true
    } );
} );