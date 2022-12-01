import { input, testInput } from "./input.js";

// P1 -> Test Answer = 40
// P2 -> Test Answer = 315

const inputArr = input.split(/\n/).map((row) => row.split("").map(Number));

const neighbours = [
  [1, 0],
  [0, 1],
  [-1, 0],
  [0, -1],
];

// Part 1

const sortQueue = (queue) => {
  return queue.sort((a, b) => a.risk - b.risk);
};

const shortestPath = (grid, start = [0, 0]) => {
  const xLength = grid[0].length - 1;
  const yLength = grid.length - 1;

  const queue = [{ point: start, risk: 0 }];
  const visitedNode = new Set();

  while (queue.length) {
    const {
      point: [x, y],
      risk,
    } = queue.shift();

    if (y === yLength && x === xLength) return risk;

    let neighbourPoints = neighbours.map(([curX, curY]) => [
      curX + x,
      curY + y,
    ]);

    let filteredPoints = neighbourPoints
      .filter(([x, y]) => grid[y]?.[x])
      .filter((position) => !visitedNode.has(position + ""));

    filteredPoints.forEach((position) => {
      visitedNode.add(position + "");
      queue.push({
        point: position,
        risk: risk + grid[position[1]][position[0]],
      });
    });

    sortQueue(queue);
  }
};

console.log(shortestPath(inputArr), "Part 1");

// Part 2

//////////////////////////////////////////////////////////////
// Not my solution, from reddit thread, hence commented out and not submitted answer

// const expandedPath = (grid) => {
//   const expandedGrid = [...Array(grid.length * 5)].map((_, y) =>
//     [...Array(grid[0].length * 5)].map(
//       (_, x) =>
//         1 +
//         ((grid[y % grid.length][x % grid[0].length] -
//           1 +
//           Math.trunc(x / grid[0].length) +
//           Math.trunc(y / grid.length)) %
//           9)
//     )
//   );
//   return expandedGrid;
// };

// const part2Grid = expandedPath(inputArr);
// console.log(shortestPath(part2Grid), "Part 2");

/////// Version 1 & Start of Dijkstra ///////

// const generateGrid = (maxX, maxY) => {
//   return Array(maxY + 1)
//     .fill()
//     .map(() => Array(maxX + 1).fill(0));
// };

// let riskGrid = generateGrid(xLength - 1, yLength - 1);

// for (let y = 0; y < yLength; y++) {
//   for (let x = 0; x < xLength; x++) {
//     if (x === 0 && y === 0) {
//       riskGrid[y][x] = 0;
//     } else {
//       let path = [];
//       if (x > 0) {
//         path.push(riskGrid[y][x - 1]);
//       }
//       if (y > 0) {
//         path.push(riskGrid[y - 1][x]);
//       }
//       riskGrid[y][x] = Math.min(...path) + grid[y][x];
//     }
//   }
// }

// console.table(riskGrid);
// console.log(riskGrid[yLength - 1][xLength - 1]);

// const map = inputArr;
// const startNode = grid[0][0];
// const finishNode = grid[grid.length - 1][grid[0].length - 1];
// // console.log(startNode, finishNode);

// const allNodes = (grid) => grid.reduce((acc, val) => acc.concat(val));
// console.log(allNodes(inputArr));
