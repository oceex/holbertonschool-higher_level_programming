#!/usr/bin/node
exports.callMeMoby = function (x, thefunction) {
  while (x) {
    thefunction();
    x -= 1;
  }
};
