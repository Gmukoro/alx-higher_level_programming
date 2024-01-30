#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let t = 0;
  while ((len - t) > 0) {
    const aux = list[len];
    list[len] = list[t];
    list[t] = aux;
    t++;
    len--;
  }
  return list;
};
