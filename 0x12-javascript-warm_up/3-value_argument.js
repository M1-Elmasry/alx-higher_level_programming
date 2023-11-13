#!/usr/bin/node

// import process module and get argv
const argv = process.argv;

if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
