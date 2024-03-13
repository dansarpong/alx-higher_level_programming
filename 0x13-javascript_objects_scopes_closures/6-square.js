#!/usr/bin/node
// a class Square that defines a square and inherits from Square of 5-square.js
'use strict';

const SquarePast = require('./5-square');

module.exports = class Square extends SquarePast {
  charPrint (c) {
    let i = 0;
    let j = 0;
    let str = '';
    if (!c) {
      c = 'X';
    }
    for (i = 0; i < this.width; i++) {
      str += c;
    }
    for (j = 0; j < this.height; j++) {
      console.log(str);
    }
  }
};
