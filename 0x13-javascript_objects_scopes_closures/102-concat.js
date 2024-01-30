#!/usr/bin/node
const { readFileSync, writeFile } = require('fs');
const { argv } = require('process');

const getContent = (file) => {
  return readFileSync(file, 'utf8');
};

const concatenated = getContent(argv[2]) + '' + getContent(argv[3]);

writeFile(argv[4], concatenated, 'utf8', err => {
  if (err) throw err;
});
