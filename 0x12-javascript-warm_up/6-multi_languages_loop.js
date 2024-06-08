#!/usr/bin/node
const arg = process.argv;
for (let i=2; i <= arg.length - 1; i++) {
  console.log(arg[i]);
}
