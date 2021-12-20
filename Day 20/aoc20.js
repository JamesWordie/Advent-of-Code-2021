import { input, testInput, algorithm, testAlgo } from "./input.js";

let inputArr = input.split(/\n/).map((row) => row.split(""));

// console.table(inputArr);

const convertBinary = (arr) => {
  let binaryArr = arr.map((char) => {
    return char === "." ? 0 : 1;
  });
  return parseInt(binaryArr.join(""), 2);
};

const getNeighbours = (y, x, t, inputArray) => {
  let neighbourArr = [];
  for (let j = -1; j <= 1; j++) {
    for (let i = -1; i <= 1; i++) {
      if (
        x + i < 0 ||
        y + j < 0 ||
        x + i > inputArray[0].length - 1 ||
        y + j > inputArray.length - 1
      ) {
        neighbourArr.push((algorithm[0] && t % 2) === 0 ? "." : "#");
      } else {
        // console.log(y + j, x + i, "yj - xi");

        neighbourArr.push(inputArray[y + j][x + i]);
      }
    }
  }
  //   console.log(algorithm[0] && t % 2);
  //   console.log(neighbourArr, "neighbour");
  return neighbourArr;
};

// console.log(getNeighbours(0, 0, inputArr));

const countArr = (arr) => {
  let counter = 0;
  for (let j = 0; j < arr.length; j++) {
    for (let i = 0; i < arr[0].length; i++) {
      if (arr[j][i] === "#") counter++;
    }
  }
  return counter;
};

// const resetBorder = (arr) => {
//   let copy = [...arr];
//   for (let j = 0; j < arr.length; j++) {
//     for (let i = 0; i < arr[0].length; i++) {
//       if (
//         j === 0 ||
//         j === arr.length - 1 ||
//         i === 0 ||
//         i === arr[0].length - 1
//       ) {
//         // copy[j][i] = ".";
//         if (copy[j][i] === ".") {
//           copy[j][i] = algorithm[0] === "." ? "." : "#";
//         } else {
//           copy[j][i] = algorithm[algorithm.length - 1] === "#" ? "#" : ".";
//         }
//       }
//     }
//   }
//   return copy;
// };

const solver = (inputArray, loops) => {
  let tmp = [];
  for (let t = 0; t < loops; t++) {
    let newImgArr = [];
    for (let y = -1; y < inputArray.length + 1; y++) {
      let newImgArrRow = [];
      for (let x = -1; x < inputArray[0].length + 1; x++) {
        // console.log(y, x, t, inputArray);
        let neighbourArr = getNeighbours(y, x, t, inputArray);
        let algoIndex = convertBinary(neighbourArr);
        let newPixel = algorithm[algoIndex];
        newImgArrRow.push(newPixel);
      }
      newImgArr.push(newImgArrRow);
    }
    tmp = newImgArr;
    inputArray = newImgArr;
  }
  //   console.log(tmp);
  return countArr(tmp);
};

let newImgArrs = solver(inputArr, 2);
let newImgArrsP2 = solver(inputArr, 50);
// console.log(part1(inputArr, 2));

console.log(newImgArrs, "Part 1");
console.log(newImgArrsP2, "Part 2");
