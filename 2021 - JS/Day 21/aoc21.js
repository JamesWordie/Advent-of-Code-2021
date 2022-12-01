// test positions -> 4, 8
// input positions -> 7, 1

// P1 -> player 1 wins, 993 rolls, player2 score = 745, result = 745*993 = 739785
// P2 -> player1 -> 444356092776315, player2 -> 341960390180808, score > 21

// spaces 1 -> 10 inclusive, wrap
// 3 rolls at a time
// when score hits 1000 end
// track rolls, score & positions

let player1 = {
  score: 0,
  position: 7,
};

let player2 = {
  score: 0,
  position: 1,
};

let scores = {
  p1: 0,
  p2: 0,
};

let rolls = 0;
let dicePosition = 1;

const calcPosition = (player, rolls) => {
  player.position = ((player.position - 1 + rolls) % 10) + 1;
  player.score += player.position;
};

const rollDie = () => {
  rolls += 1;
  let total = dicePosition;
  dicePosition += 1;
  if (dicePosition > 100) {
    dicePosition = 1;
  }
  return total;
};

const part1 = () => {
  let currentPlayer = player1;

  while (player1.score < 1000 && player2.score < 1000) {
    let rollScore = [rollDie(), rollDie(), rollDie()].reduce(
      (acum, curr) => (acum += curr)
    );

    calcPosition(currentPlayer, rollScore);

    currentPlayer = currentPlayer === player1 ? player2 : player1;
  }

  return Math.min(player1.score, player2.score) * rolls;
};

// console.log(part1());

//////// Part 2 is not my solution and I have not submitted, for learning purpose ///////////

function part2() {
  player1 = {
    position: 7,
    score: 0,
  };
  player2 = {
    position: 1,
    score: 0,
  };
  console.log(splitUniverse(player1, player2, true));
}

function splitUniverse(p1, p2, p1Turn) {
  if (p1.score >= 21) {
    return 1;
  } else if (p2.score >= 21) {
    return 0;
  }

  const currPlayer = p1Turn ? p1 : p2;
  let sum = 0;
  for (let diceOutcome = 3; diceOutcome <= 9; diceOutcome++) {
    const oldPos = currPlayer.position;
    const oldScore = currPlayer.score;
    calcPosition(currPlayer, diceOutcome);
    const multiplier = diceDistribution(diceOutcome);
    sum += multiplier * splitUniverse(p1, p2, !p1Turn);
    currPlayer.position = oldPos;
    currPlayer.score = oldScore;
  }
  return sum;
}

function diceDistribution(num) {
  switch (num) {
    case 3:
      return 1; // 111
    case 4:
      return 3; // 112, 121, 211
    case 5:
      return 6; // 113, 131, 311, 122, 212, 221
    case 6:
      return 7; // 123, 132, 213, 231, 312, 321, 222
    case 7:
      return 6; // 223, 232, 322, 133, 313, 331
    case 8:
      return 3; // 233, 323, 332
    case 9:
      return 1; // 333
  }
}

part2();
