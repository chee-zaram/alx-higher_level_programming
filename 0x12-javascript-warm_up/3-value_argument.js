#!/usr/bin/node
// print the first argument passed to the script
// if no argument is passed, prints a message to the console

const argv = require('process').argv;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
