#!/usr/bin/node
// Class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
