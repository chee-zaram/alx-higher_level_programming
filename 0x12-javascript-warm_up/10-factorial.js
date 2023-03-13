#!/usr/bin/node
// computes and prints factorial of a number supplied as command-line argument

const argv = require('process').argv;
const number = parseInt(argv[2]);

function factorial (number) {
  if (isNaN(number) || number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(number));
