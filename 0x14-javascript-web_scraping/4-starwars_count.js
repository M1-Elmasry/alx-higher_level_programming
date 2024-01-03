#!/usr/bin/node

const request = require('request');

const baseUrl = process.argv[2];
const characterId = '18';

request.get(baseUrl, undefined, (err, _res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body).results;
    const moviesIdPresents = data.filter((movie) => {
      return movie.characters.some((item) => item.endsWith(`${characterId}/`));
    });
    const idPresentsCount = moviesIdPresents.length;
    console.log(idPresentsCount);
  }
});
