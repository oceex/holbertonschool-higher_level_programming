#!/usr/bin/node
const headers = document.querySelectorAll('header');
const div = document.querySelector('#red_header');
div.addEventListener('click', e => { headers.forEach(header => { header.classList.add('red'); }); });
