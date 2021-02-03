#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const argv1 = process.argv[2];
const argv2 = process.argv[3];
console.log(add(argv1, argv2));
