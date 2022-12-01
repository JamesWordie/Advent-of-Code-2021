import { input, testInput } from "./input.js";

// P1 -> Test Result 17 Dots after 1 fold

const points = [];
const folds = [];

const filterInput = input.split(/\n/).map((row) => {
  if (row.match(/\d,\d/)) {
    points.push(row.split(",").map(Number));
  } else {
    folds.push(
      row
        .split(" ")[2]
        .split("=")
        .map((fold) => (fold.match(/\d/) ? Number.parseInt(fold) : fold))
    );
  }
});

// console.log(points, "coords");
// [
//   [6, 10],
//   [0, 14],
//   [9, 10],
//   [0, 3],
//   [10, 4],
//   [4, 11],
//   [6, 0],
//   [6, 12],
//   [4, 1],
//   [0, 13],
//   [10, 12],
//   [3, 4],
//   [3, 0],
//   [8, 4],
//   [1, 10],
//   [2, 14],
//   [8, 10],
//   [9, 0],
// ];
// console.log(folds, "folds");
// [ [ 'y', 7 ], [ 'x', 5 ] ]

const [maxX, maxY] = points.reduce(([maxX, maxY], [x, y]) => {
  return [Math.max(x, maxX), Math.max(y, maxY)];
});

const generateGrid = (maxX, maxY) => {
  return Array(maxY + 1)
    .fill()
    .map(() => Array(maxX + 1).fill(0));
};

const grid = generateGrid(maxX, maxY);
// console.table(generateGrid(maxX, maxY));

const fillGrid = (grid, points) => {
  let populatedGrid = [...grid];
  for (let [x, y] of points) {
    populatedGrid[y][x] = 1;
  }
  return populatedGrid;
};

const mappedGrid = fillGrid(grid, points);
// console.table(fillGrid(grid, points));
let newGrid = [...mappedGrid];

const foldPaper = (fold) => {
  const [axis, foldLine] = fold;

  if (axis === "y") {
    for (let y = 0; y < foldLine; y++) {
      for (let x = 0; x < newGrid[y].length; x++) {
        newGrid[y][x] = newGrid[y][x] | newGrid[2 * foldLine - y]?.[x];
      }
    }
    newGrid.length = foldLine;
  } else {
    for (let y = 0; y < newGrid.length; y++) {
      for (let x = 0; x < foldLine; x++) {
        newGrid[y][x] = newGrid[y][x] | newGrid[y][2 * foldLine - x];
      }
      newGrid[y].length = foldLine;
    }
  }
  return newGrid;
};

let foldedPaper = foldPaper(folds[0]); // Part 1 puzzle input

const part1 = () => {
  let count = 0;
  foldedPaper.map((row) => row.map((col) => (col === 1 ? count++ : null)));
  console.log(count, "Part 1");
};

part1();

// Part 2

const part2 = folds.map((fold) => {
  let tmpGrid = foldPaper(fold);
  //   console.table(tmpGrid);
  console.log(
    tmpGrid
      .map((row) => row.map((point) => (point ? "#" : " ")).join(""))
      .join("\n"),
    "Part 2"
  );
});
