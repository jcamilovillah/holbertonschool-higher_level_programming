#!/usr/bin/node
let nExec = 0;
exports.logMe = function (item) {
  console.log('%d: %s', nExec++, item);
};
