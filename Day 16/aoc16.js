import {
  input,
  testInput,
  testInputOperator0,
  testInputOperator1,
} from "./input.js";

/**
 * 1st 3 bits -> packet version
 * 2nd 3 bits -> packet type ID, 4: literal value, padded 0 until multiple 4 length
 * prefixed with 1 or 0, 0 being last group of 5 bits
 * any type ID !== 4 are operator packets
 * bit immediately after packet header (1st 6 bits), length type ID
 * length type ID = 0 or 1, 0 -> the next 15 bits represent total length in bits of sub-packets
 * 1 -> next 11 bits represent number sub packets immediately container
 */

/**
8A004A801A8002F478 represents an operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of 16.
620080001611562C8802118E34 represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12.
C0015000016115A2E0802F182340 has the same structure as the previous example, but the outermost packet uses a different length type ID. This packet has a version sum of 23.
A0016C880162017C3686B18A3D4780 is an operator packet that contains an operator packet that contains an operator packet that contains five literal values; it has a version sum of 31.
 */

const bitChars = {
  0: "0000",
  1: "0001",
  2: "0010",
  3: "0011",
  4: "0100",
  5: "0101",
  6: "0110",
  7: "0111",
  8: "1000",
  9: "1001",
  A: "1010",
  B: "1011",
  C: "1100",
  D: "1101",
  E: "1110",
  F: "1111",
};

const hexToBinary = input
  .split("")
  .map((char) => bitChars[char.toUpperCase()])
  .join("");
// console.log(hexToBinary);

const typeCases = (type, num, subValues) => {
  if (type === 0) {
    return (num = subValues.reduce((a, v) => a + v, 0));
  } else if (type === 1) {
    return (num = subValues.reduce((a, v) => a * v, 1));
  } else if (type === 2) {
    return (num = Math.min(...subValues));
  } else if (type === 3) {
    return (num = Math.max(...subValues));
  } else if (type === 5) {
    return (num = subValues[0] > subValues[1] ? 1 : 0);
  } else if (type === 6) {
    return (num = subValues[0] < subValues[1] ? 1 : 0);
  } else if (type === 7) {
    return (num = subValues[0] === subValues[1] ? 1 : 0);
  }

  return num;
};

const typeFour = (total, position, version, input) => {
  position = 6;
  input = input.substr(6);
  let moreBits = true;
  while (moreBits) {
    moreBits = input[0] === "1";
    total = total * 16 + Number.parseInt(input.substr(1, 4), 2);
    position += 5;
    input = input.substr(5);
  }
  return [total, version, position];
};

////////////////////// FROM REDDIT - TO FURTHER MY LEARNING < NOT SUBMITTED AS NOT MINE ///////////////

function readPacket(str) {
  let version = parseInt(str.substr(0, 3), 2);
  let type = parseInt(str.substr(3, 3), 2);

  let num = 0;
  let pos = 0;

  if (type === 4) {
    return typeFour(num, pos, version, str);
  }

  let subValues = [];

  if (str[6] === "0") {
    let length = parseInt(str.substr(7, 15), 2);
    let sub = str.substr(22, length);
    while (sub.length > 0) {
      let res = readPacket(sub);
      subValues.push(res[0]);
      version += res[1];
      sub = sub.substr(res[2]);
    }
    pos += 22 + length;
  } else {
    let packets = parseInt(str.substr(7, 11), 2);
    pos = 18;
    let sub = str.substr(18);
    for (let i = 0; i < packets; i++) {
      let res = readPacket(str.substr(pos));
      subValues.push(res[0]);
      version += res[1];
      pos += res[2];
      sub = sub.substr(res[2]);
    }
  }

  num = typeCases(type, num, subValues);

  return [num, version, pos];
}

let [part2, part1] = readPacket(hexToBinary);
console.log(part1, "Part 1");
console.log(part2, "Part 2");
