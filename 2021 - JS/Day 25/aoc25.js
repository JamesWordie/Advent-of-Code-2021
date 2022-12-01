import { input, testInput } from "./input.js";

let inputArr = input.split(/\n/).map((row) => row.split(""));
// console.table(inputArr);

let WIDTH = inputArr.length;
const HEIGHT = inputArr[0].length;
const RIGHT = ">";
const DOWN = "v";
const FREE = ".";

const moveRight = () => {
  let rightCounter = 0;
  let moves = [];
  for (let y = 0; y < WIDTH; y++) {
    for (let x = 0; x < HEIGHT; x++) {
      if (checkNeighbour(y, x, RIGHT)) {
        moves.push([y, x]);
        rightCounter++;
      }
    }
  }

  makeMove(moves, RIGHT);
  return rightCounter;
};

const moveDown = () => {
  let downCounter = 0;
  let moves = [];
  for (let y = 0; y < WIDTH; y++) {
    for (let x = 0; x < HEIGHT; x++) {
      if (checkNeighbour(y, x, DOWN)) {
        moves.push([y, x]);
        downCounter++;
      }
    }
  }

  makeMove(moves, DOWN);
  return downCounter;
};

const checkNeighbour = (y, x, direction) => {
  if (direction === DOWN) {
    return inputArr[y][x] === DOWN && inputArr[(y + 1) % WIDTH][x] === FREE;
  }
  if (direction === RIGHT) {
    return inputArr[y][x] === RIGHT && inputArr[y][(x + 1) % HEIGHT] === FREE;
  }
};

const makeMove = (moves, direction) => {
  for (let pair of moves) {
    let [y, x] = pair;
    inputArr[y][x] = FREE;
    if (direction === RIGHT) {
      inputArr[y][(x + 1) % HEIGHT] = RIGHT;
    } else if (direction === DOWN) {
      inputArr[(y + 1) % WIDTH][x] = DOWN;
    }
  }
};

const part1 = () => {
  let counter = 0;
  while (true) {
    counter++;
    let total = moveRight() + moveDown();
    if (total === 0) {
      break;
    }
  }
  return counter;
};

console.log(part1());
