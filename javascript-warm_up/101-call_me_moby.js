#!/usr/bin/node
exports.callMeMoby = function (x, thefunction) {
  while (x > 0) {
    thefunction();
    x -= 1;
  }
};
