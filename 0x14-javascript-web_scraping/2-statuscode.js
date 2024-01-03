#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, undefined, (err, res, _body) => {
  if (err) console.log(err);
  else console.log('code: ' + res.statusCode);
});
