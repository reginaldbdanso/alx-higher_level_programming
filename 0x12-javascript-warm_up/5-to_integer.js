#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else if (process.argv[2] < 0) {
  // pass
} else {
  console.log(parseInt(process.argv[2]));
}
