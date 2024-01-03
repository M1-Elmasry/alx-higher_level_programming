#!/usr/bin/node

const request = require('request');

const baseUrl = process.argv[2];
const characterId = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(baseUrl, undefined, (err, _res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body).results;
    const moviesIdPresents = data.filter((movie) => {
      return movie.characters.includes(characterId);
    });
    const idPresentsCount = moviesIdPresents.length;
    console.log(idPresentsCount);
  }
});
