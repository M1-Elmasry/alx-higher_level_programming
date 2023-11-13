#!/usr/bin/node

// import process module and get argv
const argv = process.argv;
const input = argv[2];

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  n = parseInt(n);

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(input));
