import { input } from "./input.js";

let [w, x, y, z] = [0, 0, 0, 0];

const sortCommands = input.split(/\n/).map((row) => {
  let tmp = row.match(/(\w{3})\s{1}(\d{1})\s(\d?)/g);
  console.log(tmp);
});

console.log(sortCommands);

const filterInput = (input) => {};
