#!/usr/bin/node

const { existsSync, statSync, readFileSync, createWriteStream } = require('fs');
const args = require('process').argv;
const fileA = args[2];
const fileB = args[3];
const dest = args[4];

function concat () {
  if (
    existsSync(fileA) &&
    statSync(fileA).isFile &&
    existsSync(fileB) &&
    statSync(fileB).isFile &&
    dest !== undefined
  ) {
    const fileAData = readFileSync(fileA);
    const fileBData = readFileSync(fileB);
    const fd = createWriteStream(dest);

    fd.write(fileAData);
    fd.write(fileBData);
    fd.end();
  } else {
    console.error(`usage: ${args[1]} fileA fileB dest`);
  }
}

concat();
