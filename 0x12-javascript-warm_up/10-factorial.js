#!/usr/bin/node
function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
let num;
if (isNaN(process.argv[2])) {
  num = 1;
} else {
  num = process.argv[2];
}
console.log(factorial(num));
