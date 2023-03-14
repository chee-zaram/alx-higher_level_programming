#!/usr/bin/node
// prints the number of arguments already printed and the new argument value

let index = 0;

exports.logMe = function (item) {
  console.log(`${index++}: ${item}`);
};
