#!/usr/bin/node
const ls = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.count; i++) {
      const item = document.createElement('li');
      item.textContent = data.results[i].title;
      ls.appendChild(item);
    }
  });
