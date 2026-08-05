#!/usr/bin/node
let c = 2;
const x = [];
if (process.argv.length <= 2) {
  console.log(0);
} else {
  while (process.argv[c]) {
    x.push(parseInt(process.argv[c]));
    c += 1;
  }
  x.sort((a, b) => a - b);
  console.log(x[x.length - 2]);
}
