import { input, testInput, testInput1, testInput2 } from "./input.js";

// P1 -> 10 Paths, P2 -> 36 Paths

// P1 -> 19 Paths, P2 -> 103 Paths

// P1 -> 226 Paths, P2 -> 3509 Paths

// Part 1

const inputArr = input.split(/\n/).map((row) => row.trim().split("-"));
// console.log(inputArr);

const generateMap = (inputArr) => {
  let caveMap = {};

  for (let row of inputArr) {
    const [start, end] = row;

    // start coord in caveMap already?
    start in caveMap ? caveMap[start].push(end) : (caveMap[start] = [end]);
    // end coord in caveMap already?
    end in caveMap ? caveMap[end].push(start) : (caveMap[end] = [start]);
  }

  return caveMap;
};

// console.log(generateMap(inputArr));

const isSmallCave = (position, path) => {
  return position.toLowerCase() === position && path.includes(position);
};

const part1 = () => {
  const caveMap = generateMap(inputArr);
  let paths = [];

  const findPaths = (point, path = []) => {
    const nextPath = [...path, point];

    if (point === "end") {
      paths.push(nextPath);
      return;
    }

    caveMap[point].forEach((pos) => {
      if (isSmallCave(pos, path)) return;

      findPaths(pos, nextPath);
    });
  };

  findPaths("start");

  let numPaths = paths.length;

  return numPaths;
};

console.log(part1(), "Part 1");

// Part 2
