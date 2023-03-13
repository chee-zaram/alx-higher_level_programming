#!/usr/bin/node
// prints the addition of the first two arguments

const argv = require('process').argv;
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
    return;
  }
  console.log(a + b);
}

add(num1, num2);
