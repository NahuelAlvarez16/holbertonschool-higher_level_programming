#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  if (error)
    console.log(error);

  fs.writeFile(argv[1], body, (error, data) => {
    if (error) {
      console.error(error);
    }
  });
});
