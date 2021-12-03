const test = `down 4
down 3
up 8
down 9
up 2
up 5
forward 2
forward 5
forward 8
up 7
forward 4
forward 2
forward 2
forward 3`;

const pair = test.split(/\n/);

// console.log(pair);

const move = pair.map((movement) => movement.split(" "));

let horizontal = 0; // 26
let depth = 0; //-51
let aim = 0; //-6

const formatNum = (strNum) => Number.parseInt(strNum);

const formatted = move.forEach((m) => {
	switch (m[0]) {
		case "forward":
			horizontal += formatNum(m[1]);
			depth += aim * formatNum(m[1]);
			break;
		case "down":
			// depth += formatNum(m[1]);
			aim += formatNum(m[1]);
			break;
		case "up":
			// depth -= formatNum(m[1]);
			aim -= formatNum(m[1]);
			break;
		default:
			break;
	}
});

console.log(horizontal, "forward");

console.log(depth, "down");

console.log(aim, "aim");

console.log(horizontal * depth, "total");

// const pair = test.split(/\n/);

// // console.log(pair);

// const move = pair.map((movement) => movement.split(" "));

// let horizontal = 0; // 26
// let depth = 0; // -6
// // let up = 0; // -6

// const formatted = move.forEach((m) => {
// 	switch (m[0]) {
// 		case "forward":
// 			horizontal += Number.parseInt(m[1]);
// 			break;
// 		case "down":
// 			depth += Number.parseInt(m[1]);
// 			break;
// 		case "up":
// 			depth -= Number.parseInt(m[1]);
// 			break;
// 		default:
// 			break;
// 	}
// });

// console.log(horizontal, "forward");

// console.log(depth, "down");

// // console.log(up, "up");

// console.log(horizontal * depth);
