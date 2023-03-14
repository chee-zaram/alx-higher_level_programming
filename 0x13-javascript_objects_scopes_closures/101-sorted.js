#!/usr/bin/node
// mports a dictionary of occurrences by user id and
// computes a dictionary of user ids by occurrence.

const dict = require('./101-data').dict;

function sortedDict (dict) {
  const newDict = {};
  Object.getOwnPropertyNames(dict).forEach((occurrence) => {
    if (newDict[dict[occurrence]] === undefined) {
      newDict[dict[occurrence]] = [occurrence];
    } else {
      newDict[dict[occurrence]].push(occurrence);
    }
  });
  console.log(newDict);
}

sortedDict(dict);
