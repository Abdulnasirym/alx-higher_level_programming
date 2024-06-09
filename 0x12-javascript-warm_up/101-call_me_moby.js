#!/usr/bin/node
exports.callMeboy = function(x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
