#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let arrSort = process.argv.sort((a, b) => a - b);
  console.log(arrSort[arrSort.length - 2]);
}
