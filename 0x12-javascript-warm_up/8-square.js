#!/usr/bin/node
// print a square based on the number passed in as the first command-line argument

const argv = require('process').argv;
const length = parseInt(argv[2]);
const arr = [];

if (!isNaN(argv[2])) {
  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      arr.push('X');
    }
    if (i !== length - 1) {
      arr.push('\n');
    }
  }
  if (length > 0) {
    console.log(arr.join(''));
  }
} else {
  console.log('Missing size');
}
