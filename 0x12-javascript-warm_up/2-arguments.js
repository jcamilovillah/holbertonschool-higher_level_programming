#!/usr/bin/node
// prints a message depending of the number of arguments passed
if (process.argv.length < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
