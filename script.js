
// Function to create the Sudoku board
function createBoard(containerId, editable = true) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';
  for (let i = 0; i < 81; i++) {
    const cell = document.createElement('div');
    cell.className = 'sudoku-cell';
    if (editable) {
      const input = document.createElement('input');
      input.type = 'number';
      input.min = 1;
      input.max = 9;

      // Add event listener for input change
      input.addEventListener('change', (event) => {
        const value = parseInt(event.target.value);
        if (value === 0 || isNaN(value)) {
          alert('Invalid Input: 0 is not allowed in Sudoku!');
          event.target.value = ''; // Clear the input field
        }
      });

      cell.appendChild(input);
    }
    container.appendChild(cell);
  }
}

// Function to get the board state from input fields
function getBoardState() {
  const board = [];
  const inputs = document.querySelectorAll('#input-board input');
  for (let i = 0; i < 9; i++) {
    const row = [];
    for (let j = 0; j < 9; j++) {
      const value = inputs[i * 9 + j].value;
      row.push(value === '' ? null : parseInt(value));
    }
    board.push(row);
  }
  return board;
}

// Function to display the solution
function displaySolution(board) {
  const solutionBoard = document.getElementById('solution-board');
  solutionBoard.innerHTML = '';
  solutionBoard.style.display = 'grid';
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      const cell = document.createElement('div');
      cell.className = 'sudoku-cell';

      // Add bold borders
      if (i % 9 === 2 || i % 9 === 5 || i % 9 === 8) {
        cell.classList.add('bold-right');
      }
      if (i % 3 === 0) {
        cell.classList.add('bold-left');
      }
      if (i >= 18 && i <= 26 || i >= 45 && i <= 53) {
        cell.classList.add('bold-bottom');
      }

      cell.textContent = board[i][j];
      solutionBoard.appendChild(cell);
    }
  }
}

// Event listener for the solve button
document.getElementById('solve-button').addEventListener('click', () => {
  const board = getBoardState();
  const solution = solve(board);
  if (solution) {
    displaySolution(solution);
  } else {
    alert('No solution found!');
  }
});

// Create the input board when the page loads
window.onload = () => {
  createBoard('input-board');
};