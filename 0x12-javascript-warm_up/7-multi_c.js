#!/usr/bin/node
const value = process.argv[2];

if (!parseInt(value)) {
  console.log("Missing number of occurences");
} else {
  for (let i = 0; i < value; i++) {
    console.log("C is fun");
  }
}
