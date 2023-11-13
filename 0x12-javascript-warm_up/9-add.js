#!/usr/bin/node

// import process module and get argv
const argv = process.argv;
const firstArg = parseInt(argv[2]);
const secondArg = parseInt(argv[3]);

console.log(`${firstArg + secondArg}`);
