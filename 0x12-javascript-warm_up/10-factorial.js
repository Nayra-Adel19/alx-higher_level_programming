#!/usr/bin/node
function factorial (b) {
  return (b === 0 || isNaN(b) ? 1 : b * factorial(b - 1));
}
console.log(factorial(Number(process.argv[2])));
