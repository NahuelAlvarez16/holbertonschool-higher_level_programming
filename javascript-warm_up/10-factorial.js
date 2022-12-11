#!/usr/bin/node

const argv = process.argv;

function factorial (number) {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}
console.log(factorial(parseInt(argv[2]) || 1));
