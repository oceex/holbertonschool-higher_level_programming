#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  const add = document.querySelector('#add_item');
  const remove = document.querySelector('#remove_item');
  const clear = document.querySelector('#clear_list');
  const list = document.querySelector('.my_list');
  add.addEventListener('click', () => {
    const child = document.createElement('li');
    child.textContent = 'Item';
    list.appendChild(child);
  });
  remove.addEventListener('click', () => {
    list.lastElementChild.remove();
  });
  clear.addEventListener('click', () => {
    while (list.firstChild) {
      list.removeChild(list.firstChild);
    }
  });
});
