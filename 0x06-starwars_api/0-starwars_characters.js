#!/usr/bin/node
const request = require('request');

function getMovieData (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/films/${movieId}`;

    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(`Failed to retrieve data for Movie ID ${movieId}`);
      }
    });
  });
}

async function printCharacterNames (movieId) {
  try {
    const movieData = await getMovieData(movieId);

    if (movieData) {
      const characters = movieData.characters;
      for (const characterUrl of characters) {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            console.log(JSON.parse(body).name);
          } else {
            console.error(`Failed to retrieve character data for URL: ${characterUrl}`);
          }
        });
      }
    } else {
      console.log('No characters found for the specified movie ID.');
    }
  } catch (error) {
    console.error(error);
  }
}

// Extract Movie ID from command line arguments
const movieId = process.argv[2];

// Check if Movie ID is provided
if (movieId) {
  // Call the function with the provided Movie ID
  printCharacterNames(movieId);
} else {
  console.error('Please provide a Movie ID as a command line argument (e.g., star_wars.js 3)');
}
