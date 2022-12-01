import { input, testInput, testInput1 } from "./input.js";

const inputArr = input.split(/\n/).map((row) => row.split(" "));

// console.log(inputArr);

function filterInput(arr) {
  let vals = [];
  arr.map((line) => {
    let command = line[0];
    let numArrs = line[1]
      .split(/[\(a-z)=]/)
      .filter((res) => res !== "")
      .map((itm) => itm.split(".."));

    let nums = numArrs.map((pairs) => pairs.map((num) => Number.parseInt(num)));
    let x = nums[0].sort((a, b) => a - b);
    let y = nums[1].sort((a, b) => a - b);
    let z = nums[2].sort((a, b) => a - b);

    // console.log(x, y, z, "x, y, z");
    if (
      x[0] < -50 ||
      x[1] > 50 ||
      y[0] < -50 ||
      y[1] > 50 ||
      z[0] < -50 ||
      z[1] > 50
    ) {
      vals;
    } else {
      vals.push([command, x, y, z]);
    }
  });
  return vals;
}

// console.log(filterInput(inputArr));
const commands = filterInput(inputArr);

const part1 = (commands) => {
  let uniqSet = new Set();
  commands.map((row) => {
    for (let x = row[1][0]; x < row[1][1] + 1; x++) {
      for (let y = row[2][0]; y < row[2][1] + 1; y++) {
        for (let z = row[3][0]; z < row[3][1] + 1; z++) {
          if (row[0] === "on") {
            uniqSet.add(`${x}-${y}-${z}`);
          } else if (row[0] === "off") {
            uniqSet.delete(`${x}-${y}-${z}`);
          }
        }
      }
    }
  });

  return uniqSet.size;
};
console.time("start");
console.log(part1(commands));
console.timeEnd("start");
