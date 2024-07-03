const b = null; // this is to show an empty space on the board

const bd1 = [ // 2d array to show the board with all empty spaces
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b]
];

const bd2 = [ // this board is to show how a real board might look like
    [b,b,b,b,b,b,b,b,1],
    [5,b,b,b,b,b,2,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,9,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,4,b,b,3,b,b],
    [b,b,b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b,b,9]
];

const bd3 = [ // this board is impossible to solve 
    [1,2,3,4,5,6,7,8,b],
    [b,b,b,b,b,b,b,b,2],
    [b,b,b,b,b,b,b,b,3],
    [b,b,b,b,b,b,b,b,4],
    [b,b,b,b,b,b,b,b,5],
    [b,b,b,b,b,b,b,b,6],
    [b,b,b,b,b,b,b,b,7],
    [b,b,b,b,b,b,b,b,8],
    [b,b,b,b,b,b,b,b,9]
];

function solve(board) {
    if (solved(board)) {
        return board;
    } else {
        const possibilities = nextBoards(board);
        const validBoards = keepOnlyValid(possibilities);
        return searchForSolution(validBoards); // helper function
    }
}

// uses backtracking
function searchForSolution(boards) {
    if (boards.length < 1) {
        return false;
    } else {
        // backtracking search for solution
        const first = boards.shift();
        const tryPath = solve(first);
        if (tryPath !== false) {
            return tryPath;
        } else {
            return searchForSolution(boards);
        }
    }
}

function solved(board) {
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            if (board[i][j] === null) {
                return false;
            }
        }
    }
    return true;
}

function nextBoards(board) {
    var res = [];
    const firstEmpty = findEmptySquare(board); // should return a set of coordinates
    if (firstEmpty != undefined) {
        const y = firstEmpty[0];
        const x = firstEmpty[1];
        for (var i = 1; i <= 9; i++) {
            var newBoard = board.map(row => row.slice()); // deep copy of the board
            newBoard[y][x] = i;
            res.push(newBoard);
        }
    }
    return res;
}

function findEmptySquare(board) {
    // board -> return a tuple with 2 elements like coordinates [Int, Int]
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            if (board[i][j] === null) {
                return [i, j];
            }
        }
    }
}

function keepOnlyValid(boards) {
    return boards.filter(b => validBoard(b));
}

function validBoard(board) {
    return rowGood(board) && columnGood(board) && boxesGood(board);
}

function rowGood(board) {
    for (var i = 0; i < 9; i++) {
        var cur = [];
        for (var j = 0; j < 9; j++) {
            if (cur.includes(board[i][j])) {
                return false;
            } else if (board[i][j] != null) {
                cur.push(board[i][j]);
            }
        }
    }
    return true;
}

function columnGood(board) { // same code as rowGood except [i][j] are switched to [j][i]
    for (var i = 0; i < 9; i++) {
        var cur = [];
        for (var j = 0; j < 9; j++) {
            if (cur.includes(board[j][i])) {
                return false;
            } else if (board[j][i] != null) {
                cur.push(board[j][i]);
            }
        }
    }
    return true;
}

function boxesGood(board) {
    const boxCoordinates = [
        [0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2]
    ];

    for (var y = 0; y < 9; y += 3) {
        for (var x = 0; x < 9; x += 3) {
            var cur = [];
            for (var i = 0; i < 9; i++) {
                var coordinates = [...boxCoordinates[i]];
                coordinates[0] += y;
                coordinates[1] += x;
                if (cur.includes(board[coordinates[0]][coordinates[1]])) {
                    return false;
                } else if (board[coordinates[0]][coordinates[1]] != null) {
                    cur.push(board[coordinates[0]][coordinates[1]]);
                }
            }
        }
    }
    return true;
}

console.log(solve(bd1));
