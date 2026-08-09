#!/usr/bin/node
const char = document.querySelector('#character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(res => res.json())
  .then(data => {
    char.textContent = data.name;
  });
