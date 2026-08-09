#!/usr/bin/node
const headers = document.querySelectorAll('header');
const div = document.querySelector('#toggle_header');
div.addEventListener('click',
  e => {
    headers.forEach(header => {
      if (header.classList.contains('red')) {
        header.classList.toggle('red');
        header.classList.add('green');
      } else {
        header.classList.toggle('green');
        header.classList.add('red');
      }
    });
  });
