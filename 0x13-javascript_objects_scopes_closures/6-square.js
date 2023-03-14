#!/usr/bin/node
// defines a `Square` which inherits from `Rectangle`

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
