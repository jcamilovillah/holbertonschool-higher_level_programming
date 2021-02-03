#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (process.argv[2]) {
  const x = process.argv[2];
  for (let i = 0; i < x; i++) {
    for (let i = 0; i < x; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
