#!/usr/bin/node
const fetch = require('node-fetch');
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;

  try {
    const response = await fetch(endpoint);
    if (!response.ok) {
      throw new Error(`Error fetching film data: ${response.statusText}`);
    }
    const filmData = await response.json();
    const characters = filmData.characters;

    for (const url of characters) {
      const charResponse = await fetch(url);
      if (!charResponse.ok) {
        throw new Error(`Error fetching character data: ${charResponse.statusText}`);
      }
      const character = await charResponse.json();
      console.log(character.name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

starwarsCharacters(filmID);
