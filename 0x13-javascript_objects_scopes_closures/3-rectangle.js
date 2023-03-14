#!/usr/bin/node
// defines a rectangle based on width and height

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) < 1 || parseInt(h) < 1) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
