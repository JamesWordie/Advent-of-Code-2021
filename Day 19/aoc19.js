import { input } from "./input.js";

// function sumBy(array, validator) {
//   return Array.prototype.reduce.call(
//     array,
//     (accum, element, index) => accum + validator(element, index),
//     0
//   );
// }

// const parseScanner = (txt) => {
//   const lines = txt.split("\n");
//   const beacons = lines
//     .slice(1)
//     .map((l) => l.split(",").map((part) => parseInt(part, 10)));
//   return {
//     beacons,
//     distances: beacons.map((b1) => beacons.map((b2) => dist(b1, b2))),
//   };
// };

// const dist = (p1, p2) =>
//   Math.sqrt(sumBy([(p1, p2)], ([a, b]) => (a - b) * (a - b)));

// const inputArr = input.split(/\n\n/).map(parseScanner);

// console.log(inputArr);
