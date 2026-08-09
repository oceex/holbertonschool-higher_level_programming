#!/usr/bin/node
const tx = document.querySelector('#update_header');
const header = document.querySelector('header');

tx.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
