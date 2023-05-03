// Fetch from an api and translate

const htmlDoc = $(document);
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
const htmlTag = 'DIV#hello';

const translateHello = (result) => $(htmlTag).text(result.hello);

const ajaxGet = () => {
  $.ajax({
    url: URL,
    type: 'GET',
    success: translateHello
  });
};

htmlDoc.ready(ajaxGet);
