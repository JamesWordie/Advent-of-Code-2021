import { input } from "./input.js";

// let [w, x, y, z] = [0, 0, 0, 0];

// const sortCommands = input.split(/\n/).map((row) => {
//   let tmp = row.match(/(\w{3})\s{1}(\d{1})\s(\d?)/g);
//   console.log(tmp);
// });

// console.log(sortCommands);

// const filterInput = (input) => {};

////////////// SOLUTION FROM REDDIT - NOT SUBMITTED //////////////////

function solve(input, part) {
  const lines = input.split("\n");

  const terms = [];
  for (let i = 0; i < lines.length; i += 18) {
    terms.push([4, 5, 15].map((j) => +lines[i + j].split(" ")[2]));
  }

  const prevs = [];
  const digits = [];
  for (const [i, [a, b, c]] of Object.entries(terms)) {
    if (a === 1) {
      prevs.push([i, c]);
    } else {
      const [prevI, prevC] = prevs.pop();
      const complement = prevC + b;
      digits[prevI] =
        part === 1 ? Math.min(9, 9 - complement) : Math.max(1, 1 - complement);
      digits[i] = digits[prevI] + complement;
    }
  }
  return digits.join("");
}
console.log(solve(input, 1), "Part 1");
console.log(solve(input, 2), "Part 2");
