#!/usr/bin/node

const argv = process.argv.slice(2).map((n) => {
  return parseInt(n);
});

if (!argv[0] || isNaN(argv[1])) {
  console.log('0');
} else {
  console.log(argv.sort((a, b) => {
    return a - b;
  }).reverse()[1]);
}
