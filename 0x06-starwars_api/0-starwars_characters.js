#!/usr/bin/node
const request = require("request");
const movieID = process.argv[2];
const options = {
  url: "https://swapi-api.alx-tools.com/api/films/" + movieID,
  method: "GET"
};

request(options, function (error, response, body) {
  if(!error) {
    const movieCharacters = JSON.parse(body).characters;
    displayMovieCharacters(movieCharacters, 0);
  }
});

function displayMovieCharacters (movieCharacters, index) {
  request(movieCharacters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < movieCharacters.length) {
      displayMovieCharacters(movieCharacters, index + 1);
      }
    }
  });
}
