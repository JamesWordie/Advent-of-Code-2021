// TEST INPUT target area: x=20..30, y=-10..-5
// good pairs -> (7,2) (6,3) (9,0)
// bad pairs -> (17,-4)
// best pair -> (6,9) maxY = 45
// part 2 -> 112 velocities land in target

// MY INPUT target area: x=25..67, y=-260..-200

// MY INPUT
const [minX, maxX, minY, maxY] = [25, 67, -260, -200];

// MY TEST
// const [minX, maxX, minY, maxY] = [20, 30, -10, -5];

// Part 1

// calculate the drag for the x speed
const dragX = (x) => {
  if (x === 0) return 0;
  return x > 0 ? -1 : +1;
};

// boolean to see if the tmp x and y lands in the target
const isInTarget = (tmpX, tmpY) => {
  if (tmpX >= minX && tmpX <= maxX && tmpY >= minY && tmpY <= maxY) {
    return true;
  }
  return false;
};

const probeHeight = (x, y) => {
  let tmpX = 0;
  let tmpY = 0;
  let [speedX, speedY] = [x, y];
  let maxY = 0;

  // while x is less than x2 (right side of target)
  // && y is greater than y1 (top of target)
  while (tmpX <= maxX && tmpY >= minY) {
    tmpX += speedX;
    tmpY += speedY;
    speedX += dragX(speedX); // add drag value to x speed
    // console.log(speedX);
    speedY -= 1; // -1 for gravity from y speed

    // if current Y is greater than max Y, set the value
    if (tmpY > maxY) {
      maxY = tmpY;
    }

    // is the value in the target area? return maxY
    if (isInTarget(tmpX, tmpY)) {
      return maxY;
    }
  }

  return null;
};

// console.log(probeHeight(6, 9)); // 45

// Refactor

const solve = () => {
  let totalHeight = 0;
  let counter = 0;

  for (let j = -1000; j <= 1000; j++) {
    for (let i = -1000; i <= 1000; i++) {
      let value = probeHeight(i, j);
      if (value !== null) {
        totalHeight = value;
        counter++;
      }
    }
  }
  return [totalHeight, counter];
};

const [part1Res, part2Res] = solve();
console.log(part1Res, "Part 1");
console.log(part2Res, "Part 2");

// Old //

// const part1 = () => {
//   let total = 0;

//   for (let j = -1000; j <= 1000; j++) {
//     for (let i = -1000; i <= 1000; i++) {
//       let value = probeHeight(i, j);
//       if (value !== null) {
//         total = value;
//       }
//     }
//   }
//   return total;
// };

// // console.log(part1(), "Part 1");

// // Part 2

// const part2 = () => {
//   let counter = 0;

//   for (let j = -1000; j <= 1000; j++) {
//     for (let i = -1000; i <= 1000; i++) {
//       let value = probeHeight(i, j);
//       if (value !== null) {
//         counter += 1;
//       }
//     }
//   }
//   return counter;
// };

// console.log(part2(), "Part 2");
