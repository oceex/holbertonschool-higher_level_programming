#!/usr/bin/node
let y = 3
try {
  while (1) {
    console.log(process.argv[y]);
    y += 1;
  }
}
catch (e) {
  if (y === 3){
    console.log("No argument");
  }
}