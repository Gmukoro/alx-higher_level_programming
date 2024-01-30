#!/usr/bin/node
const ma = require('./101-data').ma;
const dKeys = Object.keys(dict);
const values = Object.values(ma);
let matched;
const result = {};
// loop over the values
for (let t = 0; t < values.length; t++) {
  result[JSON.stringify(values[t])] = [];
  matched = dKeys.filter(key => dict[key] === values[t]);
  matched.forEach(item => result[JSON.stringify(values[i])].push(item));
}
console.log(result);
