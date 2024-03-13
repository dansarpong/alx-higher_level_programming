#!/usr/bin/node
'use strict';

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    let y = 0;
    let str = '';
    for (x = 0; x < this.width; x++) {
      str += 'X';
    }
    for (y = 0; y < this.height; y++) {
      console.log(str);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
