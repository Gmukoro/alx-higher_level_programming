#!/usr/bin/node
const dict = require('./101-data').dict;
const dKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const result = {};
// loop over the values
for (let t = 0; t < values.length; t++) {
  result[JSON.stringify(values[t])] = [];
  matched = dKeys.filter(key => dict[key] === values[t]);
  matched.forEach(item => result[JSON.stringify(values[t])].push(item));
}
console.log(result);
