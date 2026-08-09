#!/usr/bin/node
const adding = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

adding.addEventListener('click', () => {
  const child = document.createElement('li');
  child.textContent = 'Item';
  list.appendChild(child);
});
