$(document).ready(function () {
    $('#btn_translate').click(function () {
        const langCode = $('#language_code').val();
    
        const APIurl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
        $.get(APIurl, function(data) {
            $('DIV#hello').html(data.hello);
        });
    });
});