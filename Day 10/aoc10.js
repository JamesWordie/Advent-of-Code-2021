import { input, testInput } from "./input.js";

// P1 result --> 26397
// P2 result --> 288957

const inputLines = input.split(/\n/);
// console.log(inputLines);

const openBrackets = "([{<";
const closeBrackets = ")]}>";

// Part 1

const charScores = { ")": 3, "]": 57, "}": 1197, ">": 25137 };

function partOneSolve(inputLines) {
  let corruptedPart1 = 0;
  for (const line of inputLines) {
    let stack = [];
    for (const char of line) {
      const opnBrk = openBrackets.indexOf(char);
      // if -1 ie if bracket not an opening, push into stack, index of closing
      if (opnBrk !== -1) stack.push(closeBrackets[opnBrk]);
      // if char is not equal to matching pop (ie for matching pairs) add the score to corrupted
      else if (stack.pop() !== char) {
        corruptedPart1 += charScores[char];
        break;
      }
    }
  }
  return corruptedPart1;
}

const result1 = partOneSolve(inputLines);
console.log(result1, "Part 1:");

// Part 2

const inCompleteScores = { ")": 1, "]": 2, "}": 3, ">": 4 };

function partTwoSolve(inputLines) {
  let incomplete = [];
  for (const line of inputLines) {
    let stack = [];
    let corruptedPart2 = false;
    for (const char of line) {
      const opnBrk = openBrackets.indexOf(char);
      if (opnBrk !== -1) stack.push(closeBrackets[opnBrk]);
      else if (stack.pop() !== char) {
        corruptedPart2 = true;
        break;
      }
    }

    if (!corruptedPart2 && stack.length > 0) {
      let tmpChar = 0;
      for (const c of stack.reverse()) {
        tmpChar = tmpChar * 5 + inCompleteScores[c];
      }
      incomplete.push(tmpChar);
    }
  }

  let result = incomplete.sort((a, b) => a - b)[
    Math.floor(incomplete.length / 2)
  ];
  return result;
}

const result2 = partTwoSolve(inputLines);
console.log(result2, "Part 2:");
