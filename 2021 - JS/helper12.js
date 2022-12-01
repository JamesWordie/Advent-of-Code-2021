export const part2 = (input) => {
  const map = createMap(input);

  let paths = [];

  const findPaths = (label, path = [], flag = false) => {
    const nextPath = [...path, label];

    if (label === END) {
      paths.push(nextPath);
      return;
    }

    map[label].forEach((nextLabel) => {
      if (nextLabel === START) return;

      let nextFlag = flag;

      const charCode = nextLabel.charCodeAt(0);
      if (charCode >= 97) {
        if (path.includes(nextLabel)) {
          if (nextFlag) return;
          nextFlag = true;
        }
      }

      findPaths(nextLabel, nextPath, nextFlag);
    });
  };

  findPaths(START);

  return paths.length;
};
