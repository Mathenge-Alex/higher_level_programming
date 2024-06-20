#!/usr/bin/node
const firstArgs = process.argv[2];
if (firstArgs === undefined || isNaN(firstArgs)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgs; i++) {
    console.log('C is fun');
  }
}
