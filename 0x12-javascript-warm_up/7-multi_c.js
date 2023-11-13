#!/usr/bin/node

// import process module and get argv
const argv = process.argv;
const printTimes = parseInt(argv[2]);

if (!printTimes) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < printTimes; i++) {
  console.log('C is fun');
}
