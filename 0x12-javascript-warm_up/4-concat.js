#!/usr/bin/node
// concatenates two arguments passed to the script and prints them

const argv = require('process').argv;
console.log(argv[2] + ' is ' + argv[3]);
