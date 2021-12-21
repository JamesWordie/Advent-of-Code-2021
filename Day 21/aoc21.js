// test positions -> 4, 8
// input positions -> 7, 1

// P1 -> player 1 wins, 993 rolls, player2 score = 745, result = 745*993 = 739785

// spaces 1 -> 10 inclusive, wrap
// 3 rolls at a time
// when score hits 1000 end
// track rolls, score & positions

const player1 = {
  score: 0,
  position: 7,
};

const player2 = {
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

console.log(part1());
