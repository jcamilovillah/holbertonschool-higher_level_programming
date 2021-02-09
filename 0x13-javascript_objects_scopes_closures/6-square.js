#!/usr/bin/node
const inhe = require('./5-square.js');
module.exports = class Square extends inhe {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let iter = 0; iter < this.width; iter++) {
      console.log(c.repeat(this.width));
    }
  }
};
