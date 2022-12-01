import { input, testInput } from "./input.js";

const inputArr = input.split(/\n/).map((row) => row.split("").map(Number));

const x = inputArr.length;
const y = inputArr[0].length;

let lowPoint = [];

const adj = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1],
];
let count = 0;
let pointSet = new Set();

function* neighbors(i, j) {
  for (const [adjI, adjJ] of adj) {
    if (
      i + adjI < x &&
      i + adjI > -1 &&
      j + adjJ < y &&
      j + adjJ > -1 &&
      !pointSet.has(1000 * (i + adjI) + j + adjJ)
    )
      yield [i + adjI, j + adjJ];
  }
}
for (let i = 0; i < x; i++) {
  for (let j = 0; j < y; j++) {
    let maxVal = Infinity;
    for (const [currI, currJ] of neighbors(i, j)) {
      maxVal = Math.min(maxVal, +inputArr[currI][currJ]);
    }
    if (+inputArr[i][j] < maxVal) {
      count += +inputArr[i][j] + 1;
      lowPoint.push([i, j]);
    }
  }
}
console.log(count, "Part 1");
