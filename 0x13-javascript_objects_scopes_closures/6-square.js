#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let p = '';
      for (let t = 0; t < this.width; t++) {
        p += c;
      }
      console.log(p);
    }
  }
}

module.exports = Square;
