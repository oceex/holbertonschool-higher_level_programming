#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x) {
  console.log('My number: ' + x);
} else {
  console.log('Not a number');
}
