#!/usr/bin/node
/* prints all characters of a Star Wars movie: */
const request = require('request');

// Function to make a request and return a promise
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to print character names for a given film
async function printCharacterNames (movieId) {
  try {
    // Fetch film data
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    const filmData = await makeRequest(filmUrl);

    // Extract character URLs from the film data
    const characterURLs = filmData.characters;

    // Fetch and print character names concurrently
    const characterNames = await Promise.all(
      characterURLs.map(async (charUrl) => {
        const characterData = await makeRequest(charUrl);
        return characterData.name;
      })
    );

    // Print the names of all characters
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Check if the Movie ID is provided as a command line argument
if (process.argv.length >= 3) {
  const movieId = process.argv[2];
  printCharacterNames(movieId);
}
