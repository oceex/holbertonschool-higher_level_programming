#!/usr/bin/node
let y = 2
while (process.argv[y] !== undefined) {
    console.log(process.argv[y]);
    y += 1;
}
if (y === 2){
    console.log("No argument");
}
