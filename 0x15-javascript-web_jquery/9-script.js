const APIurl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function() {  
    $.get(APIurl, function(data) {
        $('#hello').text(data.hello);
    });
});