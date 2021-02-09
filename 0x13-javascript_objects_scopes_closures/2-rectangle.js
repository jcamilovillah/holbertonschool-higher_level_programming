#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.height = h;
    this.width = w;
  }
};
