function showCountryForZip() {
    var mode = $("#modeOfSearch").find(":selected").val();
    if(mode === 'Zip') {
        $("#country").show(1000);
        $("#country").prop("required", true);
    } else {
        $("#country").hide(1000);
        $("#country").removeAttr('required');
    }
}

$(document).ready(function(){

    showCountryForZip();

    // If mode of Search is changed from anything to Zip
    // For that add an click eventListner to select
    $("#modeOfSearch").click(function(){
        showCountryForZip();
    });
});