#!/usr/bin/node
// defines a rectangle based on width and height

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const line = 'X'.repeat(this.width);
      console.log(line);
    }
  }
}

module.exports = Rectangle;
