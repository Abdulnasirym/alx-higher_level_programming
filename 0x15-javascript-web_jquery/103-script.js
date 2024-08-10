$(document).ready(function() {
    function translateHello() {
        const val = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${val}`;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(function (){
        translateHello();
    });

    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            translateHello();
        }
    });
});