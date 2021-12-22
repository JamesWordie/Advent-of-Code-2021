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
    // vals.push([command, x[0], x[1], y[0], y[1], z[0], z[1]]);
  });
  return vals;
}

// console.log(filterInput(inputArr));
const commands = filterInput(inputArr);

const part1 = (commands) => {
  let setRes = new Map();
  let uniqSet = new Set();
  commands.map((row) => {
    for (let x = row[1][0]; x < row[1][1] + 1; x++) {
      for (let y = row[2][0]; y < row[2][1] + 1; y++) {
        for (let z = row[3][0]; z < row[3][1] + 1; z++) {
          if (row[0] === "on") {
            // setRes.set([x, y, z], "on");
            uniqSet.add(`${x}-${y}-${z}`);
          } else if (row[0] === "off") {
            // setRes.set([x, y, z], "off");
            // for (let itm of uniqSet) {
            //   console.log(typeof itm);
            //   itm === [x, y, z]
            //     ? uniqSet.delete([x, y, z])
            //     : uniqSet.add([x, y, z]);
            // }
            // console.log(uniqSet.has([x, y, z]));
            uniqSet.delete(`${x}-${y}-${z}`);
          }
        }
      }
    }
  });

  //   console.log(uniqSet.size);
  return uniqSet.size;

  //   let counter = {};
  //   for (let item of setRes) {
  //     if (item[1] === "on") {
  //       !(item[0].toString() in counter)
  //         ? (counter = { ...counter, [item[0].toString()]: 1 })
  //         : (counter[item[0].toString()] += 1);
  //     } else {
  //       !(item[0].toString() in counter)
  //         ? (counter = { ...counter, [item[0].toString()]: -1 })
  //         : (counter[item[0].toString()] -= 1);
  //     }
  //   }

  //   let c;
  //   c = Object.values(counter).filter((i) => i === 1 || i === 0);
  //   return c.length;
};
console.time("start");
console.log(part1(commands));
console.timeEnd("start");
