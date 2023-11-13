#!/usr/bin/node

// import process module and get argv
const argv = process.argv;
const printTimes = parseInt(argv[2]);

if (!printTimes) {
  console.log('Missing size');
}

for (let i = 0; i < printTimes; i++) {
  console.log('X'.repeat(printTimes));
}
