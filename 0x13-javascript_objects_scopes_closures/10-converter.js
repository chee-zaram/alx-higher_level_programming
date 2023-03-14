#!/usr/bin/node
// converts a number to a new base from base 10

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
