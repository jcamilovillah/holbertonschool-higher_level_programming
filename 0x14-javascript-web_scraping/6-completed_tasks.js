#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  const dict = {};
  let count = 1;
  let primero = json[0].userId;
  for (const userd of json) {
    const saveId = userd.userId;
    if (userd.completed) {
      if (primero !== userd.userId) {
        primero = userd.userId;
        count = 1;
      }
      dict[saveId] = count++;
    }
  }
  console.log(dict);
});
