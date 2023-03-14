#!/usr/bin/node
// computes a new array from another array and prints both

const list = require('./100-data').list;

function computeArray (list) {
  const newList = list.map((item, index) => item * index++);
  console.log(list);
  console.log(newList);
}

computeArray(list);
