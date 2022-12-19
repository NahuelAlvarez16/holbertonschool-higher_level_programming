#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  let count = 0;
  const data = JSON.parse(body);
  for (const mv of data.results) {
    for (const character of mv.characters) {
      const id = character.split('/')[5];
      if (id === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
