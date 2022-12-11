#!/usr/bin/node

const argv = process.argv.slice(2);

if (!argv[0] || isNaN(argv[1])) {
  console.log('0');
} else {
  console.log(argv.sort().reverse()[1]);
}
