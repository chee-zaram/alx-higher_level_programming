// Adds a <li> element to a list when the user clicks on tag `DIV#add_item`

const htmlDoc = $(document);
const item = '<li>Item</li>';
const ulClass = $('UL.my_list');
const addItemDiv = $('DIV#add_item');
const addAnItem = () => ulClass.append(item);

htmlDoc.ready(addItemDiv.on('click', addAnItem));
