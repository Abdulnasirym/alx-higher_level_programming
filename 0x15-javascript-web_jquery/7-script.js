const APIurl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(APIurl, function(data) {
    $('#character').text(data.name);
});