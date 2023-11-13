#!/usr/bin/node

// import process module and get argv
const argv = process.argv;
const argvLength = argv.length;

if (argvLength === 2) {
  console.log(0);
} else if (argvLength === 3) {
  console.log(0);
} else if (argvLength > 3) {
  // get all numbers
  const numbers = argv.slice(2);
  // convert all string number to numbers and sort the array
  const sortedNumbers = numbers.map((num) => parseInt(num, 10)).sort((a, b) => b - a);
  // print second biggest number
  console.log(sortedNumbers[1]);
}
