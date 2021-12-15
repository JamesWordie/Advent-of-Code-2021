import { input, testInput, testInput1 } from "./input.js";

const inputArr = input.split(",").map((num) => Number.parseInt(num));

function mapping(input) {
  //   let copy = [...input];
  let copy = [];
  for (num of input) {
    if (num === 0) {
      copy.push(6);
      copy.push(8);
    } else {
      copy.push(num - 1);
    }
  }

  return copy;
}

function part1(input, days) {
  let copy = [...input];
  for (let i = 0; i < days; i++) {
    copy = mapping(copy);
  }

  return copy;
}

const result = part1(inputArr, 80);

console.log(result.length);

function part2(input) {
  const counter = Array(10).fill(0);

  input.forEach((num) => {
    counter[num]++;
  });

  for (let day = 0; day < 256; day++) {
    const fish0 = counter[0];
    for (let i = 0; i <= 8; i++) {
      counter[i] = counter[i + 1];
    }
    counter[8] = fish0;
    counter[6] += fish0;
  }

  return counter.reduce((tot, curr) => tot + curr);
}

console.log(part2(inputArr));
