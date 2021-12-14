const input = `KFFNFNNBCNOBCNPFVKCP
PB -> F
KC -> F
OB -> H
HV -> N
FS -> S
CK -> K
CC -> V
HF -> K
VP -> C
CP -> S
HO -> N
OS -> N
HS -> O
HB -> F
OH -> V
PP -> B
BS -> N
VS -> F
CN -> B
KB -> O
KH -> B
SS -> K
NS -> B
BP -> V
FB -> S
PV -> O
NB -> S
FC -> F
VB -> P
PC -> O
VF -> K
BV -> K
OO -> B
PN -> N
NH -> H
SP -> B
KF -> O
BN -> F
OF -> C
VV -> H
BB -> P
KN -> H
PO -> C
BH -> O
HC -> B
VO -> O
FV -> B
PK -> V
KO -> H
BK -> V
SC -> S
KV -> B
OV -> S
HK -> F
NP -> V
VH -> P
OK -> S
SO -> C
PF -> C
SH -> N
FP -> V
CS -> C
HH -> O
KK -> P
BF -> S
NN -> O
OC -> C
CB -> O
BO -> V
ON -> F
BC -> P
NO -> N
KS -> H
FF -> V
FN -> V
HP -> N
VC -> F
OP -> K
VN -> S
NV -> F
SV -> F
FO -> V
PS -> H
VK -> O
PH -> P
NF -> N
KP -> S
CF -> S
FK -> P
FH -> F
CO -> H
SN -> B
NC -> H
SK -> P
CV -> P
CH -> H
HN -> N
SB -> H
NK -> B
SF -> H`;

const testInput = `NNCB
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C`;

// Template:     NNCB
// After step 1: NCNBCHB
// After step 2: NBCCNBBBCBHCB
// After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
// After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
// 10 steps - 3073 length, B-1749, C-298, H-161, N-865
// most - least => 1749 - 161 = 1588

let template;
let inputObj = {};

const formatInput = testInput.split(/\n/).map((row, index) => {
  if (index === 0) {
    template = row;
  } else {
    let splitRow = row.split(" -> ");
    inputObj[splitRow[0]] = splitRow[1];
  }
});

// console.log(template, "template");
// console.log(inputObj, "object");

// Part 1

const mutateTmp = (temp) => {
  let next = temp[0];
  for (let i = 1; i < temp.length; i++) {
    let group = temp.substr(i - 1, 2);
    if (inputObj[group] !== null) {
      next += inputObj[group];
    }
    next += temp[i];
  }
  return next;
};

for (let i = 0; i < 10; i++) {
  template = mutateTmp(template);
}

const countChars = (tempString) => {
  let counter = {};
  tempString
    .split("")
    .map((char) => (counter[char] = (counter[char] ?? 0) + 1));
  //  OLD VERSION, DIRTY
  // .map((char) => {
  //   !(`${char}` in counter)
  //     ? (counter = { ...counter, [`${char}`]: +1 })
  //     : (counter[`${char}`] += 1);
  // });
  return counter;
};

const charTotal = countChars(template);
const charValues = Object.values(charTotal);
// console.log(countChars(template));

const [minChar, maxChar] = [Math.min(...charValues), Math.max(...charValues)];

console.log(maxChar - minChar, "Part 1");

// Part 2

//////////////////////////////////////////////////////////////
// Not my solution, from reddit thread, hence commented out and not submitted answer
// I don't know what to do hence left as this.

// let newTemplate = input.split(/\n/).slice(0, 1)[0];
// let rules = input.split(/\n/).slice(1);

// const nextPairs = rules.reduce((acc, rule) => {
//   const [left, right] = rule.split(" -> ");
//   acc[left] = [left[0] + right, right + left[1]];
//   return acc;
// }, {});

// console.log(nextPairs);

// let pairCounts = {};
// for (let i = 0; i < newTemplate.length - 1; i++) {
//   const pair = newTemplate.slice(i, i + 2);
//   pairCounts[pair] = (pairCounts[pair] ?? 0) + 1;
// }
// console.log(pairCounts);

// for (let step = 0; step < 40; step++) {
//   const nextCounts = {};
//   for (const pair in pairCounts) {
//     for (const nextPair of nextPairs[pair]) {
//       nextCounts[nextPair] = (nextCounts[nextPair] ?? 0) + pairCounts[pair];
//     }
//   }
//   pairCounts = nextCounts;
// }
// console.log(pairCounts);

// const elCounts = {
//   [newTemplate[0]]: 1,
// };
// console.log(elCounts);

// for (const pair in pairCounts) {
//   elCounts[pair[1]] = (elCounts[pair[1]] ?? 0) + pairCounts[pair];
// }

// const elCountValues = Object.values(elCounts);
// console.log(Math.max(...elCountValues) - Math.min(...elCountValues));

////////////////////////////////////////////////////////////////////////
// For my input to the puzzle -> Part 2 - 2158894777814
