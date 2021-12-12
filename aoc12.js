const input = `we-NX
ys-px
ys-we
px-end
yq-NX
px-NX
yq-px
qk-yq
pr-NX
wq-EY
pr-oe
wq-pr
ys-end
start-we
ys-start
oe-DW
EY-oe
end-oe
pr-yq
pr-we
wq-start
oe-NX
yq-EY
ys-wq
ys-pr`;

const testInput = `start-A
start-b
A-c
A-b
b-d
A-end
b-end`;

// P1 -> 10 Paths, P2 -> 36 Paths

const testInput1 = `dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc`;

// P1 -> 19 Paths, P2 -> 103 Paths

const testInput2 = `fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW`;

// P1 -> 226 Paths, P2 -> 3509 Paths

// Part 1

const inputArr = input.split(/\n/).map((row) => row.trim().split("-"));
// console.log(inputArr);

const generateMap = (inputArr) => {
  let caveMap = {};

  for (let row of inputArr) {
    const [start, end] = row;

    // start coord in caveMap already?
    start in caveMap ? caveMap[start].push(end) : (caveMap[start] = [end]);
    // end coord in caveMap already?
    end in caveMap ? caveMap[end].push(start) : (caveMap[end] = [start]);
  }

  return caveMap;
};

// console.log(generateMap(inputArr));

const isSmallCave = (position, path) => {
  return position.toLowerCase() === position && path.includes(position);
};

const part1 = () => {
  const caveMap = generateMap(inputArr);
  let paths = [];

  const findPaths = (point, path = []) => {
    const nextPath = [...path, point];

    if (point === "end") {
      paths.push(nextPath);
      return;
    }

    caveMap[point].forEach((pos) => {
      if (isSmallCave(pos, path)) return;

      findPaths(pos, nextPath);
    });
  };

  findPaths("start");

  let numPaths = paths.length;

  return numPaths;
};

console.log(part1(), "Part 1");

// Part 2
