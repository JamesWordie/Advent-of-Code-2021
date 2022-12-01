import { input, testInput } from "./input.js";

const numbers = {
  0: "abcefg",
  1: "cf",
  2: "acdeg",
  3: "acdfg",
  4: "bcdf",
  5: "abdfg",
  6: "abdefg",
  7: "acf",
  8: "abcdefg",
  9: "abcdfg",
};

const splitInp = input
  .split(/\n/)
  .map((row) => row.split("|"))
  .map((row) => row.map((item) => item.trim()));

// console.table(splitInp);

let counter = 0;

let digits = [];

splitInp.map((row) => digits.push(row[1]));

const eachVal = digits.map((row) => row.split(" "));

eachVal.map((row) =>
  row.map((item) => {
    if (
      item.length === 2 ||
      item.length === 3 ||
      item.length === 4 ||
      item.length === 7
    ) {
      counter++;
    }
  })
);

// console.log(counter);

/// Correct Solution

let lines = [];
input.split("\n").forEach((x) => {
  let each = x.split(" | ");
  lines.push({ inVal: each[0].split(" "), outVal: each[1].split(" ") });
});

let sum = 0;

for (let i = 0; i < lines.length; i++) {
  let decode = new Array(10);
  decode[1] = lines[i].inVal.find((x) => x.length == 2);
  decode[4] = lines[i].inVal.find((x) => x.length == 4);
  decode[7] = lines[i].inVal.find((x) => x.length == 3);
  decode[8] = lines[i].inVal.find((x) => x.length == 7);
  decode[3] = lines[i].inVal.find((x) => {
    let split = x.split("");
    let z = decode[7].split("");
    return (
      split.length == 5 &&
      split.filter((value) => !z.includes(value)).length == 2
    );
  });
  decode[5] = lines[i].inVal.find((x) => {
    let split = x.split("");
    let z = decode[4].split("");
    return (
      split.length == 5 &&
      split.filter((value) => !z.includes(value)).length == 2 &&
      x != decode[3]
    );
  });
  decode[2] = lines[i].inVal.find(
    (x) => x.length == 5 && x != decode[3] && x != decode[5]
  );
  decode[6] = lines[i].inVal.find((x) => {
    let split = x.split("");
    let z = decode[1].split("");
    return (
      split.length == 6 &&
      split.filter((value) => !z.includes(value)).length == 5
    );
  });
  decode[9] = lines[i].inVal.find((x) => {
    let split = x.split("");
    let z = decode[4].split("");
    return (
      split.length == 6 &&
      split.filter((value) => !z.includes(value)).length == 2 &&
      x != decode[6]
    );
  });
  decode[0] = lines[i].inVal.find(
    (x) => x.length == 6 && x != decode[6] && x != decode[9]
  );
  decode.forEach((x, i) => {
    decode[i] = x.split("").sort().join("");
  });

  let number = "";
  lines[i].outVal.forEach((x) => {
    number += decode.indexOf(x.split("").sort().join(""));
  });
  sum += parseInt(number);
}

console.log(sum);
