#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (x){
    while(x) {
        console.log("C is fun");
        x -= 1;
    }
} else {
    console.log("Missing number of occurrences");
}