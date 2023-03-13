#!/usr/bin/node
// print a string using a number the first command-line argument if it can be
// converted to a number

const argv = require('process').argv;
const prefix = 'My number:';

if (!isNaN(argv[2])) {
  console.log(prefix, argv[2]);
} else {
  console.log('Not a number');
}
