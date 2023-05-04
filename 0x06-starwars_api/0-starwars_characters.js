#!/usr/bin/node
const https = require('https');

const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  https.get(`${API_URL}/films/${process.argv[2]}/`, (res) => {
    let data = '';

    res.on('data', (chunk) => {
      data += chunk;
    });

    res.on('end', () => {
      const charactersURL = JSON.parse(data).characters;
      const charactersName = charactersURL.map(
        (url) =>
          new Promise((resolve, reject) => {
            https.get(url, (res) => {
              let data = '';

              res.on('data', (chunk) => {
                data += chunk;
              });

              res.on('end', () => {
                resolve(JSON.parse(data).name);
              });

              res.on('error', (err) => {
                reject(err);
              });
            });
          })
      );

      Promise.all(charactersName)
        .then((names) => console.log(names.join('\n')))
        .catch((allErr) => console.error(allErr));
    });

    res.on('error', (err) => {
      console.error(err);
    });
  });
}

