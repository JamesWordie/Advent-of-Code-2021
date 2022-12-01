import { input, testInput } from "./input.js";

const inputArr = input.split(/\n/).map((row) => row.split("").map(Number));
// console.table(inputArr);

// P1 --> 1656 flash (test)

// Part 1

const checkSurround = (grid, row, column, flashed = new Set()) => {
  if (row < 0 || row >= grid.length) return;
  if (column < 0 || column >= grid[0].length) return;
  if (flashed.has(`${row}${column}`)) return;

  const value = grid[row][column];
  const newVal = value + 1;
  grid[row][column] = newVal;
  if (newVal <= 9) {
    return;
  }

  flashed.add(`${row}${column}`);
  grid[row][column] = 0;
  for (let i = -1; i < 2; i++) {
    for (let j = -1; j < 2; j++) {
      if (i === 0 && j === 0) {
        continue;
      }
      checkSurround(grid, row + i, column + j, flashed);
    }
  }
};

const evalArr = (grid) => {
  const flashed = new Set();
  for (let row = 0; row < grid.length; row++) {
    const rowLength = grid[row].length;
    for (let col = 0; col < rowLength; col++) {
      checkSurround(grid, row, col, flashed);
    }
  }
  return flashed.size;
};

const part1 = (input) => {
  let finalCount = 0;
  for (let i = 0; i < 100; i++) {
    finalCount += evalArr(input);
  }
  return finalCount;
};

console.log(part1(inputArr), "Part 1");

// Part 2

const part2 = (input) => {
  let count = 1;
  while (true) {
    const flashedCount = evalArr(input);
    if (flashedCount === 100) {
      break;
    }
    count++;
  }
  return count + 100;
};

console.log(part2(inputArr), "Part 2");
