#!/usr/bin/node

exports.converter = function (base) {
  return function (argv) {
	  return argv.tostring(base)
  };
};
