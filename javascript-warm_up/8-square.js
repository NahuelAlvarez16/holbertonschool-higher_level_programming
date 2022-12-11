#!/usr/bin/node

const argv = process.argv;

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
}
const size = parseInt(argv[2]);
const max = Math.pow(size, 2);
let square = '';
for (let i = 0; i < max; i++) {
  square += 'X';
  if ((i + 1) % size === 0 && i + 1 < max) {
    square += '\n';
  }
}
if (square) {
  console.log(square);
}
