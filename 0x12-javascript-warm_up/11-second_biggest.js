#!/usr/bin/node
// print the second largest integer in the list of arguments
// it is assumed that all arguments can be converted to integers

const args = require('process').argv.slice(2).map(Number);

function secondBiggest (args) {
  switch (args.length) {
    case 0:
      return 0;
    case 1:
      return 0;
  }

  let max = args[0];
  let secondMax = -Infinity;

  for (let i = 1; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax && args[i] !== max) {
      secondMax = args[i];
    }
  }

  if (secondMax === -Infinity) {
    return 0;
  }

  return secondMax;
}

console.log(secondBiggest(args));
