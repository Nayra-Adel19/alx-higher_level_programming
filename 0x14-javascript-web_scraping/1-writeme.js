#!/usr/bin/node
// The first argument is file

const fs = require('fs');

if (process.argv.length > 3) {
  fs.writeFile(process.argv[2], process.argv[3], (error) => {
    if (error) console.log(error);
  });
}
