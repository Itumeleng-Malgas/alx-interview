#!/usr/bin/node
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Define options for the HTTP request to the Star Wars API
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

/**
 * Makes a request to the Star Wars API to fetch the characters of a given movie
 * and prints each character's name sequentially.
 */
request(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

/**
 * Recursively prints the name of each character in the list.
 * @param {string[]} characters - Array of character URLs.
 * @param {number} index - Current index in the characters array.
 */
function printCharacters(characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        // Recursive call to print the next character
        printCharacters(characters, index + 1);
      }
    }
  });
}
