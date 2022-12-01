import { test, input } from "./input.js";

// let gamma = 0; //22 - most common bit
// let epsilon = 0; //9 least common bit

// let power = gamma * epsilon; //198

let sep = input.split(/\n/);
let sepTest = test.split(/\n/);

function splitInp(sep) {
  let splt = sep.map((bit) => bit.split(""));

  let counter = {};

  for (let arr = 0; arr < splt.length; arr++) {
    splt[arr].map((bit, index) => {
      if (bit === "0") {
        !(index.toString() in counter)
          ? (counter = { ...counter, [index.toString()]: -1 })
          : (counter[index.toString()] -= 1);
      } else {
        !(index.toString() in counter)
          ? (counter = { ...counter, [index.toString()]: +1 })
          : (counter[index.toString()] += 1);
      }
    });
  }

  return counter;
}

let counter = splitInp(sep);
// {
//   '0': -26,
//   '1': -30,
//   '2': 38,
//   '3': 10,
//   '4': -40,
//   '5': -10,
//   '6': 18,
//   '7': -36,
//   '8': -16,
//   '9': 40,
//   '10': -32,
//   '11': 4
// } counter

// counter < 0 therfore most common === 0
// counter > 0 therfore most common === 1

function calcCommon(counter) {
  let most = [];
  let least = [];

  for (let x = 0; x < Object.values(counter).length; x++) {
    if (counter[x.toString()] > 0) {
      most[x] = 1;
      least[x] = 0;
    } else {
      most[x] = 0;
      least[x] = 1;
    }
  }
  return [most, least];
}

let [most, least] = calcCommon(counter);
// [
//   0, 0, 1, 1, 0,
//   0, 1, 0, 0, 1,
//   0, 1
// ]

function convert(arr) {
  let strBin = arr.join("");
  let decBin = parseInt(strBin, 2);
  return decBin;
}

let gam = convert(most);
let ep = convert(least);

let pow = gam * ep;

// console.log(gam, ep, pow);

let oxy = "";

function filterInputOxy(sep) {
  let copy = [...sep];
  for (let i = 0; i < sep[0].length; i++) {
    if (copy.length === 1) {
      //   return converterBin(copy[0]);
      break;
    }

    copy = oxyFilter(i, copy);
  }
  return converterBin(copy[0]);
}

function filterInputCo2(sep) {
  let copy = [...sep];
  for (let i = 0; i < sep[0].length; i++) {
    if (copy.length === 1) {
      break;
    }
    copy = co2Filter(i, copy);
  }
  return converterBin(copy[0]);
}

function oxyFilter(ind, data) {
  let binData = [];
  for (let num of data) {
    if (!isCounter(ind, data) && num[ind] === "0") {
      binData = [...binData, num];
    } else if (isCounter(ind, data) && num[ind] === "1") {
      binData = [...binData, num];
    }
  }
  return binData;
}

function co2Filter(ind, data) {
  let binData = [];
  for (let num of data) {
    if (!isCounter(ind, data) && num[ind] === "1") {
      binData = [...binData, num];
    } else if (isCounter(ind, data) && num[ind] === "0") {
      binData = [...binData, num];
    }
  }
  return binData;
}

function isCounter(ind, data) {
  let count1 = 0;
  let count0 = 0;
  for (let bit of data) {
    if (bit[ind] === "1") {
      count1 += 1;
    } else {
      count0 += 1;
    }
  }
  if (count1 > count0 || count1 === count0) {
    return true;
  } else {
    return false;
  }
}

function reverseString(str) {
  return str.split("").reverse().join("");
}

function converterBin(binNum) {
  let reverseBinNum = reverseString(binNum);
  let decNum = 0;
  let binOp = 1;
  for (let num of reverseBinNum) {
    if (num === "1") {
      decNum += 1 * binOp;
    }
    binOp *= 2;
  }
  return decNum;
}

let oxyGen = filterInputOxy(sep);
let co2Gen = filterInputCo2(sep);

let support = oxyGen * co2Gen;

console.log(support, "support");
