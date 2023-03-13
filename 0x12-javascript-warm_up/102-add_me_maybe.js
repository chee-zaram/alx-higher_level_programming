#!/usr/bin/node
// increments `number` and calls `func`

exports.addMeMaybe = function (number, func) {
  func(++number);
};
