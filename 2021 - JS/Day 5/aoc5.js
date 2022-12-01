import { testInput, input } from "./input.js";

const inputArr = testInput
  .split(/\n/)
  .map((row) => row.split(" -> "))
  .map((row) => row.map((item) => item.split(",")));

const inputArrInt = inputArr.map((row) =>
  row.map((pair) => pair.map((item) => Number.parseInt(item)))
);
// [
//   [
//     [0, 9],
//     [5, 9],
//   ],
//   [
//     [8, 0],
//     [0, 8],
//   ],
//   [
//     [9, 4],
//     [3, 4],
//   ],
//   [
//     [2, 2],
//     [2, 1],
//   ],
//   [
//     [7, 0],
//     [7, 4],
//   ],
//   [
//     [6, 4],
//     [2, 0],
//   ],
//   [
//     [0, 9],
//     [2, 9],
//   ],
//   [
//     [3, 4],
//     [1, 4],
//   ],
//   [
//     [0, 0],
//     [8, 8],
//   ],
//   [
//     [5, 5],
//     [8, 2],
//   ],
// ];

function generateGrid(n) {
  return Array(n)
    .fill()
    .map(() => Array(n).fill(null));
}

function convertInputIntegerArray(input) {
  const inputArr = input
    .split(/\n/)
    .map((row) => row.split(" -> "))
    .map((row) => row.map((item) => item.split(",")));

  const inputArrInt = inputArr.map((row) =>
    row.map((pair) => pair.map((item) => Number.parseInt(item)))
  );
  return inputArrInt;
}

function diagonal(grid, x1, x2, y1, y2) {
  const stepX = x1 < x2 ? 1 : -1;
  const stepY = y1 < y2 ? 1 : -1;
  // console.log(x1, x2, y1, y2);
  for (let i = 0; i <= Math.abs(x1 - x2); i++) {
    const x = x1 + i * stepX;
    const y = y1 + i * stepY;
    grid[y][x] += 1;
  }
  return grid;
}

function mapLines(grid, x1, x2, y1, y2) {
  if (x1 === x2) {
    if (y1 > y2) {
      [y1, y2] = [y2, y1];
    }
    for (let j = y1; j <= y2; j++) {
      grid[j][x1] += 1;
    }
  } else if (y1 === y2) {
    // x1=0 x2=5 y1=9 y2=9
    if (x1 > x2) {
      [x1, x2] = [x2, x1];
    }
    for (let i = x1; i <= x2; i++) {
      grid[y1][i] += 1;
    }
  } else {
    diagonal(grid, x1, x2, y1, y2);
  }

  return grid;
}

function game(strInput) {
  let input = convertInputIntegerArray(strInput);
  let grid = generateGrid(1000); // change between 10 and 1000 for test vs real

  input.map((row) => {
    let [x1, y1] = row[0];
    let [x2, y2] = row[1];

    grid = mapLines(grid, x1, x2, y1, y2);
  });
  return grid;
}

const filledTable = game(input);
// console.table(filledTable);

function countTable(grid) {
  let counter = 0;
  // change between 10 and 1000 for test vs real
  for (let i = 0; i < 1000; i++) {
    for (let j = 0; j < 1000; j++) {
      if (grid[i][j] >= 2) {
        counter += 1;
      }
    }
  }
  return counter;
}

console.log(countTable(filledTable));

// let testGridEmpty = [
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// ];

// console.table(diagonal(testGridEmpty, 2, 6, 0, 4));
