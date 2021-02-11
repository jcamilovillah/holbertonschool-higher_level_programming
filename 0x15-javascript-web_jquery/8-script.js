const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const lis = data.results;
  for (const film of lis) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  }
});
