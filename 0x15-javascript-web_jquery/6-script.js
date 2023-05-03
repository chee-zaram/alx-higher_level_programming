// Update text of <header> when user clicks `DIV#update_header`

const htmlDoc = $(document);
const updateDiv = $('DIV#update_header');
const userText = 'New Header!!!';
const updateHeaderText = () => $('header').text(userText);

htmlDoc.ready(updateDiv.on('click', updateHeaderText));
