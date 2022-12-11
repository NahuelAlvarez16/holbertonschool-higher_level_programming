#!/usr/bin/node

const argv = process.argv;

if (!argv[2] || isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv[2]));
}
