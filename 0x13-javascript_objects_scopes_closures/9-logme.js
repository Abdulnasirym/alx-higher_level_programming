#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  counter++;
  console.log(`${counter - 1}: ${item}`);
};
