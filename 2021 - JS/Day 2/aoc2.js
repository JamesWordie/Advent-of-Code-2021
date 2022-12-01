import { input } from "./input.js";

const pair = input.split(/\n/);

// console.log(pair);

const move = pair.map((movement) => movement.split(" "));

let horizontal = 0;
let depth = 0;
let aim = 0;

const formatNum = (strNum) => Number.parseInt(strNum);

const formatted = move.forEach((m) => {
  switch (m[0]) {
    case "forward":
      horizontal += formatNum(m[1]);
      depth += aim * formatNum(m[1]);
      break;
    case "down":
      // depth += formatNum(m[1]);
      aim += formatNum(m[1]);
      break;
    case "up":
      // depth -= formatNum(m[1]);
      aim -= formatNum(m[1]);
      break;
    default:
      break;
  }
});

console.log(horizontal, "forward");

console.log(depth, "down");

console.log(aim, "aim");

console.log(horizontal * depth, "total");
