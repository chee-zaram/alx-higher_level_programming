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
}

module.exports = Rectangle;
