#!/usr/bin/node
const firstArg = process.argv[2];
if (firstArg === undefined || isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('X'.repeat(firstArg));
  }
}
