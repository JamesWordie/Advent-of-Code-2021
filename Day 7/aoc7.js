import { input, testInput } from "./input.js";

const inputArr = input.split(",").map(Number);

let totalNumber = inputArr.length;

function counter(input) {
  let tally = {};
  input.map((num) => {
    !(`${num}` in tally)
      ? (tally = { ...tally, [`${num}`]: +1 })
      : (tally[`${num}`] += 1);
  });
  return tally;
}

const positionHash = counter(inputArr);
// console.log(positionHash);

function median(numArray) {
  let middle = Math.floor(numArray.length / 2);
  numArray = [...numArray].sort((a, b) => a - b);
  return numArray.length % 2 !== 0
    ? numArray[middle]
    : (numArray[middle - 1] + numArray[middle]) / 2;
}

const idealPos = median(inputArr);
// console.log(median(inputArr));

function fuelCost(posHash, location) {
  let total = 0;

  for (const [key, value] of Object.entries(posHash)) {
    let keyVal = Number.parseInt(key);
    total += Math.abs(keyVal - location) * value;
  }
  return total;
}

fuelCost(positionHash, idealPos);
// console.log(fuelCost(positionHash, idealPos));

/////////////////Part 2//////////////////////

function weightedMiddle(numArray) {
  let total = numArray.reduce((accum, curr) => (accum += curr));
  let length = numArray.length;

  return Math.floor(total / length);
}

let newIdealPos = weightedMiddle(inputArr);
// console.log(weightedMiddle(inputArr));

function newFuelCost(posHash, location) {
  let total = 0;

  for (const [key, value] of Object.entries(posHash)) {
    let keyVal = Number.parseInt(key);
    let diff = Math.abs(keyVal - location);
    for (let i = 1; i <= diff; i++) {
      total += i * value;
    }
  }
  return total;
}

console.log(newFuelCost(positionHash, newIdealPos));
