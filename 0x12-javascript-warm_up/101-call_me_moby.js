#!/usr/bin/node
// execute `x` times a function passed as argument 2

exports.callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
