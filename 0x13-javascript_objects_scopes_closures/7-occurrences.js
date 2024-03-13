#!/usr/bin/node
// a function that returns the number of occurrences in a list
'use strict';

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i of list) {
    if (i === searchElement) {
      count++;
    }
  }
  return count;
};
