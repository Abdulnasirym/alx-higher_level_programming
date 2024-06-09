#!/usr/bin/node
const value = process.argv[2];
const intValue = parseInt(value);
if (isNaN(intValue)) {
    console.log("Missing number of occurences");
} else {
    for (let i = 0; i < intValue; i++) {
        console.log("C is fun");
    }
}
