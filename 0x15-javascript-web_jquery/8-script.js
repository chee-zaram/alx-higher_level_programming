// Fetches and list title of all movies from URL

const htmlDoc = $(document);
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const htmlTag = 'UL#list_movies';
const addToList = (_i, movie) => $('<li>').text(movie.title).appendTo(htmlTag);
const listMovies = (data) => $.each(data.results, addToList);

htmlDoc.ready($.getJSON(url, listMovies));
