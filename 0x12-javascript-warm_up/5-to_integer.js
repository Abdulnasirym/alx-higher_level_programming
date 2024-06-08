#!/usr/bin/node
let value = process.argv[2];
const integerValue = parseInt(value);
if (!isNaN(integerValue)) {
  console.log("My number: " + integerValue);
} else {
  console.log("Not a number");
}
