#!/usr/bin/node
// Import the 'request' module for making HTTP requests
const request = require('request')

// Get the movie ID from command line arguments
const movieId = process.argv[2]

// Define options for the HTTP request to the Star Wars API
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
}

request(options, function(error, response, body) {
  if (!error) {
    const characters=JSON.parse(body).characters
    printCharacters(characters, 0)
  }
})

function printCharacters(characters, index) {
  // Make a request to the character URL
  request(characters[index], function(error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name)
      if (index + 1 < characters.length) {
        // Recursive call to print the next character
        printCharacters(characters, index + 1)
      }
    }
  })
}
