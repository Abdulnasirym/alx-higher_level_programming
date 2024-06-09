#!/usr/bin/node
function add(a, b) {
  let sum = parseInt(process.argv[2]) + parseInt(process.argv[3]);
  console.log(sum);
}
add();
