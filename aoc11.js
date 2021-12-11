const input = `4836484555
4663841772
3512484556
1481547572
7741183422
8683222882
4215244233
1544712171
5725855786
1717382281`;

const testInput = `5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526`;

const inputArr = input.split(/\n/).map((row) => row.split("").map(Number));
// console.table(inputArr);

// P1 --> 1656 flash (test)

// Part 1

const checkSurround = (input, row, column, flashed = new Set()) => {
  if (row < 0 || row >= input.length) return;
  if (column < 0 || column >= input[0].length) return;
  if (flashed.has(`${row}${column}`)) return;

  const value = input[row][column];
  const newValue = value + 1;
  input[row][column] = newValue;
  if (newValue <= 9) {
    return;
  }

  flashed.add(`${row}${column}`);
  input[row][column] = 0;
  for (let i = -1; i < 2; i++) {
    for (let j = -1; j < 2; j++) {
      if (i === 0 && j === 0) {
        continue;
      }
      checkSurround(input, row + i, column + j, flashed);
    }
  }
};

const evalArr = (input) => {
  const flashed = new Set();
  for (let row = 0; row < input.length; row++) {
    const rowArr = input[row];
    for (let col = 0; col < rowArr.length; col++) {
      checkSurround(input, row, col, flashed);
    }
  }
  return flashed.size;
};

const part1 = (input) => {
  let totalFlashed = 0;
  for (let i = 0; i < 100; i++) {
    totalFlashed += evalArr(input);
  }
  return totalFlashed;
};

console.log("Part1");
console.log(part1(inputArr));

// Part 2

const part2 = (input) => {
  let count = 1;
  while (true) {
    const flashedCount = evalArr(input);
    if (flashedCount === 100) {
      break;
    }
    count++;
  }
  return count + 100;
};
console.log("Part2");
console.log(part2(inputArr));

// const DIRECTIONS = [
//   [-1, -1],
//   [-1, 0],
//   [-1, 1],
//   [0, -1],
//   [0, 1],
//   [1, -1],
//   [1, 0],
//   [1, 1],
// ];

// export function part1(input: string): number {
//   let flashedCount = 0;
//   const octopi = input.split("\n").map((line) =>
//     line.split("").map((char) => +char)
//   );
//   for (let step = 0; step < 100; step++) {
//     const flashed: [number, number][] = [];
//     for (let y = 0; y < octopi.length; y++) {
//       for (let x = 0; x < octopi[0].length; x++) {
//         if (++octopi[y][x] === 10) {
//           flashed.push([y, x]);
//         }
//       }
//     }
//     while (flashed.length) {
//       const [y0, x0] = flashed.pop()!;
//       flashedCount++;
//       for (const [yd, xd] of DIRECTIONS) {
//         const y1 = y0 + yd;
//         if (y1 < 0 || octopi.length <= y1) {
//           continue;
//         }
//         const x1 = x0 + xd;
//         if (x1 < 0 || octopi[0].length <= x1) {
//           continue;
//         }
//         if (++octopi[y1][x1] === 10) {
//           flashed.push([y1, x1]);
//         }
//       }
//     }
//     for (let y = 0; y < octopi.length; y++) {
//       for (let x = 0; x < octopi[0].length; x++) {
//         if (octopi[y][x] >= 10) {
//           octopi[y][x] = 0;
//         }
//       }
//     }
//   }
//   return flashedCount;
// }

// function part2(octopi) {
//   let step = 0,
//     flashedCount;
//   do {
//     step++;
//     flashedCount = 0;
//     const flashed = [];
//     for (let y = 0; y < octopi.length; y++) {
//       for (let x = 0; x < octopi[0].length; x++) {
//         if (++octopi[y][x] === 10) {
//           flashed.push([y, x]);
//         }
//       }
//     }
//     while (flashed.length) {
//       const [y0, x0] = flashed.pop();
//       flashedCount++;
//       for (const [yd, xd] of DIRECTIONS) {
//         const y1 = y0 + yd;
//         if (y1 < 0 || octopi.length <= y1) {
//           continue;
//         }
//         const x1 = x0 + xd;
//         if (x1 < 0 || octopi[0].length <= x1) {
//           continue;
//         }
//         if (++octopi[y1][x1] === 10) {
//           flashed.push([y1, x1]);
//         }
//       }
//     }
//     for (let y = 0; y < octopi.length; y++) {
//       for (let x = 0; x < octopi[0].length; x++) {
//         if (octopi[y][x] >= 10) {
//           octopi[y][x] = 0;
//         }
//       }
//     }
//   } while (flashedCount !== octopi.length * octopi[0].length);
//   return step;
// }

// console.log(part2(inputArr));
