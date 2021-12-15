import { input } from "./input.js";

const inputArr = input.split(/\n/).map(Number);

let counter = 0;

function part1(input) {
  for (let i = 1; i < input.length; i++) {
    if (input[i] > input[i - 1]) {
      counter += 1;
    }
  }
  return counter;
}

console.log(part1(inputArr));

let count = 0;

function part2(input) {
  for (let i = 3; i < input.length; i++) {
    let first = input[i] + input[i - 1] + input[i - 2];
    let second = input[i - 1] + input[i - 2] + input[i - 3];
    if (first > second) {
      count += 1;
    }
  }
  return count;
}

console.log(part2(inputArr));
