#!/usr/bin/node
const x = parseInt(process.argv[2]);
let y = '';
if (x) {
  for (let i = 1; i <= x; i++) {
    y = '';
    for (let j = 1; j <= x; j++) {
      y += 'X';
    }
    console.log(y);
  }
} else {
  console.log('Missing size');
}
