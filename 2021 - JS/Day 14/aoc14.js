import { input, testInput } from "./input.js";

// Template:     NNCB
// After step 1: NCNBCHB
// After step 2: NBCCNBBBCBHCB
// After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
// After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
// 10 steps - 3073 length, B-1749, C-298, H-161, N-865
// most - least => 1749 - 161 = 1588

let template;
let inputObj = {};

const formatInput = testInput.split(/\n/).map((row, index) => {
  if (index === 0) {
    template = row;
  } else {
    let splitRow = row.split(" -> ");
    inputObj[splitRow[0]] = splitRow[1];
  }
});

// console.log(template, "template");
// console.log(inputObj, "object");

// Part 1

const mutateTmp = (temp) => {
  let next = temp[0];
  for (let i = 1; i < temp.length; i++) {
    let group = temp.substr(i - 1, 2);
    if (inputObj[group] !== null) {
      next += inputObj[group];
    }
    next += temp[i];
  }
  return next;
};

for (let i = 0; i < 10; i++) {
  template = mutateTmp(template);
}

const countChars = (tempString) => {
  let counter = {};
  tempString
    .split("")
    .map((char) => (counter[char] = (counter[char] ?? 0) + 1));
  //  OLD VERSION, DIRTY
  // .map((char) => {
  //   !(`${char}` in counter)
  //     ? (counter = { ...counter, [`${char}`]: +1 })
  //     : (counter[`${char}`] += 1);
  // });
  return counter;
};

const charTotal = countChars(template);
const charValues = Object.values(charTotal);
// console.log(countChars(template));

const [minChar, maxChar] = [Math.min(...charValues), Math.max(...charValues)];

console.log(maxChar - minChar, "Part 1");

// Part 2

//////////////////////////////////////////////////////////////
// Not my solution, from reddit thread, hence commented out and not submitted answer
// I don't know what to do hence left as this.

// let newTemplate = input.split(/\n/).slice(0, 1)[0];
// let rules = input.split(/\n/).slice(1);

// const nextPairs = rules.reduce((acc, rule) => {
//   const [left, right] = rule.split(" -> ");
//   acc[left] = [left[0] + right, right + left[1]];
//   return acc;
// }, {});

// console.log(nextPairs);

// let pairCounts = {};
// for (let i = 0; i < newTemplate.length - 1; i++) {
//   const pair = newTemplate.slice(i, i + 2);
//   pairCounts[pair] = (pairCounts[pair] ?? 0) + 1;
// }
// console.log(pairCounts);

// for (let step = 0; step < 40; step++) {
//   const nextCounts = {};
//   for (const pair in pairCounts) {
//     for (const nextPair of nextPairs[pair]) {
//       nextCounts[nextPair] = (nextCounts[nextPair] ?? 0) + pairCounts[pair];
//     }
//   }
//   pairCounts = nextCounts;
// }
// console.log(pairCounts);

// const elCounts = {
//   [newTemplate[0]]: 1,
// };
// console.log(elCounts);

// for (const pair in pairCounts) {
//   elCounts[pair[1]] = (elCounts[pair[1]] ?? 0) + pairCounts[pair];
// }

// const elCountValues = Object.values(elCounts);
// console.log(Math.max(...elCountValues) - Math.min(...elCountValues));

////////////////////////////////////////////////////////////////////////
// For my input to the puzzle -> Part 2 - 2158894777814
