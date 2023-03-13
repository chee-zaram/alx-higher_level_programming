#!/usr/bin/node
// print a string depending on command-line arguments

const argv = require('process').argv;

switch (argv.length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
