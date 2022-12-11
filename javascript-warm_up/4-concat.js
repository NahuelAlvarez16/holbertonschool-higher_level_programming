#!/usr/bin/node

const argv = process.argv;

console.log((argv[2] || 'undefined') + ' is ' + (argv[3] || 'undefined'));
