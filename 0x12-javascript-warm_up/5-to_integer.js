#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === null) {
  console.log('Not a number');
} else if (process.argv[2] < 0) {
  // pass
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
