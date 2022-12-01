import { input, boards, testInput, testBoard } from "./input.js";

const inputArrInt = input
  .replace(/,/g, " ")
  .split(" ")
  .map((num) => Number.parseInt(num));
// [
//    7,  4,  9,  5, 11, 17, 23,  2,
//    0, 14, 21, 24, 10, 16, 13,  6,
//   15, 25, 12, 22, 18, 20,  8, 19,
//    3, 26,  1
// ]

let newArr = [];

const boardArrInt = boards
  .split(/\n/)
  .map(
    (row) => row.replace(/'  '/g, "")
    // .map((num) => Number.parseInt(num))
  )
  .map((row) => {
    if (row !== "") {
      newArr = [...newArr, row];
    }
  });

const intBoard = newArr.map((row) =>
  row
    .replace(/\s+(?=\d)/g, " ")
    .trim()
    .split(" ")
    .map((num) => Number.parseInt(num))
);

function groupArr(data, n) {
  var group = [];
  for (var i = 0, j = 0; i < data.length; i++) {
    if (i >= n && i % n === 0) j++;
    group[j] = group[j] || [];
    group[j].push(data[i]);
  }
  return group;
}

const boardsArrArr = groupArr(intBoard, 5);
// [
//   [
//     [22, 13, 17, 11, 0],
//     [8, 2, 23, 4, 24],
//     [21, 9, 14, 16, 7],
//     [6, 10, 3, 18, 5],
//     [1, 12, 20, 15, 19],
//   ],
//   [
//     [3, 15, 0, 2, 22],
//     [9, 18, 13, 17, 5],
//     [19, 8, 7, 25, 23],
//     [20, 11, 10, 24, 4],
//     [14, 21, 16, 12, 6],
//   ],
//   [
//     [14, 21, 17, 24, 4],
//     [10, 16, 15, 9, 19],
//     [18, 8, 23, 26, 20],
//     [22, 11, 13, 6, 5],
//     [2, 0, 12, 3, 7],
//   ],
// ];

const allEqual = (arr) => arr.every((val) => val === arr[0]);

function arrayCheckRow(fiveFiveArray) {
  let checkArr = [...fiveFiveArray];
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (allEqual(checkArr[j]) || allEqual(checkArr[i])) {
        return true;
      } else {
        break;
      }
    }
  }
  return false;
}

function arrayCheckCol(fiveFiveArray) {
  let checkArr = [...fiveFiveArray];
  let counter = {};
  checkArr.map((row, index) => {
    row.map((ind, rowInd) => {
      if (ind === "X") {
        // console.log(rowInd);
        // console.log(index, "index");
        !(`${rowInd}${index}` in counter)
          ? (counter = { ...counter, [`${rowInd}${index}`]: +1 })
          : (counter[`${rowInd}${index}`] += 1);
      }
    });
  });

  if (
    Object.values(counter).length === 5 &&
    Object.values(counter).every((val) => val === 1) &&
    Object.keys(counter).every((key) => key[0] === "0")
  ) {
    return true;
  }
  return false;
}

let singleTest = [
  [14, 21, 17, 24, 4],
  [10, 16, 15, 9, 19],
  [18, 8, 23, 26, 20],
  [22, 11, 13, 6, 5],
  [2, 0, 12, 3, 7],
];

let rowComplete = [
  [14, 21, 17, 24, 4],
  [10, 16, 15, 9, 19],
  ["X", "X", "X", "X", "X"],
  [22, 11, 13, 6, 5],
  [2, 0, 12, 3, 7],
];

let colDiagComplete = [
  ["X", 21, 8, 24, 4],
  [9, "X", 72, 9, 19],
  [9, 8, "X", 26, 20],
  [9, 11, 4, "X", 5],
  [9, 0, 5, 3, "X"],
];

let colComplete = [
  ["X", 21, 17, 24, 4],
  ["X", 16, 15, 9, 19],
  ["X", 8, 23, 26, 20],
  ["X", 11, 13, 6, 5],
  ["X", 0, 12, 3, 7],
];

// console.log(arrayCheckRow(colComplete));
// console.log(arrayCheckCol(colComplete));
// arrayCheckCol(colComplete);

function checkForNum(board, number) {
  let copyBoard = [...board];
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (copyBoard[i][j] === number) {
        copyBoard[i][j] = "X";
      }
    }
  }
  return copyBoard;
}

// console.log(checkForNum(singleTest, 14));

let winner;

function counterBoard(board, number) {
  let copyBoard = [...board];
  let count = 0;
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (copyBoard[i][j] !== "X") {
        count += copyBoard[i][j];
      }
    }
  }
  return count * number;
}

function game(inputArrInt, boardsArrArr) {
  let score;
  inputArrInt.map((num) => {
    boardsArrArr.forEach((board) => {
      //   console.log(board);
      let check = checkForNum(board, num);
      //   arrayCheckRow(check) && console.log(check, num);
      //   console.log(arrayCheckRow(check), "row check");
      //   console.log(arrayCheckCol(check), "col check");
      if (arrayCheckRow(check) || arrayCheckCol(check)) {
        score = counterBoard(check, num);
        console.log(score);
        return score;
      }
    });
  });
}

game(inputArrInt, boardsArrArr);
