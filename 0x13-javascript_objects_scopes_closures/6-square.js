#!/usr/bin/node
// defines a `Square` which inherits from `Rectangle`

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (c === undefined || !c) {
      c = 'X';
    } else {
      c = c.toString();
    }
    for (let i = 0; i < this.height; i++) {
      const line = c.repeat(this.width);
      console.log(line);
    }
  }
}

module.exports = Square;
