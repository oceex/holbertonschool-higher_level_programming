#!/usr/bin/node
const x = parseInt(process.argv[2]);

function factorial (x) {
  if (x > 1) {
    return x * factorial(x - 1);
  } else {
    return 1;
  }
}
console.log(factorial(x));
