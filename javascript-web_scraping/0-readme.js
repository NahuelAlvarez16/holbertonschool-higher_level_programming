#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile('./' + argv[0], (err, data) => {
  if (err) return console.error(err);
  console.log(data.toString());
});
