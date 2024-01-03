#!/usr/bin/node

const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request.get(baseUrl + id, undefined, (err, _res, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
