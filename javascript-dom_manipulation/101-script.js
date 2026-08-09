#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  const translateButton = document.getElementById('btn_translate');
  const languageSelect = document.getElementById('language_code');
  const helloElement = document.getElementById('hello');

  translateButton.addEventListener('click', () => {
    const languageCode = languageSelect.value;
    fetch(`https://hellosalut.stefanbohacek.com/?lang=${languageCode}`)
      .then((response) => response.json())
      .then((data) => {
        helloElement.innerHTML = data.hello;
      })
      .catch((error) => {
        console.error('Error fetching the translation:', error);
      });
  });
});
