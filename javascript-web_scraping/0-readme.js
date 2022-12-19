#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile('./' + argv[0], (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
