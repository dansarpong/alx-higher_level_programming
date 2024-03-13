#!/usr/bin/node
// a function that converts a number from base 10 to another base passed as argument
'use strict';

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
