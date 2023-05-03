// Fetches character name from given URL

const htmlDoc = $(document);
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const addText = (data) => $('header').text(data.name);

htmlDoc.ready($.get(url, addText));
