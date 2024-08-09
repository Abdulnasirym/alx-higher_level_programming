const APIurl = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$.get(APIurl, function(data) {
    $.each(data.results, function(index, film) {
        const listItem = $('<li>').text(film.title);
        $('#list_movies').append(listItem);
    });
});