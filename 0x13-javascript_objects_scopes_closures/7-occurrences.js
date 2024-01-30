#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let noOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      noOccurrences++;
    }
  }
  return noOccurrences;
};
