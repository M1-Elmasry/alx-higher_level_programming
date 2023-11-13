#!/usr/bin/node

// import process module and get argv
const argv = process.argv;
const firstArg = parseInt(argv[2]);

if (firstArg) {
  console.log(`My number : ${firstArg}`);
} else {
  console.log('Not a number');
}
