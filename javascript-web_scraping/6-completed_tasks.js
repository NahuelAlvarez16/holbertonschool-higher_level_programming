#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const users = {};
  const data = JSON.parse(body);
  data.forEach(element => {
    if (element.completed) {
      if (users[element.userId] == null) {
        users[element.userId] = 0;
      }
      users[element.userId] += 1;
    }
  });
  console.log(users);
});
