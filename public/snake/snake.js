// Nokia Snake Game Implementation

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

// Board configuration: 20x20 grid, each cell 20px
const gridSize = 20;
const cellSize = 20;

// Adjust canvas to fit the grid
canvas.width = gridSize * cellSize;
canvas.height = gridSize * cellSize;

// Game state variables
let snake = [{ x: Math.floor(gridSize / 2), y: Math.floor(gridSize / 2) }];
let direction = { x: 0, y: 0 };
let food = spawnFood();
let score = 0;
let intervalId;

// UI elements
const levelSelect = document.getElementById("level");
const scoreDiv = document.getElementById("score");

// Spawn food in a position not occupied by the snake
function spawnFood() {
  let pos;
  do {
    pos = {
      x: Math.floor(Math.random() * gridSize),
      y: Math.floor(Math.random() * gridSize)
    };
  } while (snake.some(seg => seg.x === pos.x && seg.y === pos.y));
  return pos;
}

// Draw the game board, snake and food
function draw() {
  // Clear board
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw snake segments
  ctx.fillStyle = "#0f0";
  snake.forEach(seg => {
    ctx.fillRect(seg.x * cellSize, seg.y * cellSize, cellSize, cellSize);
  });

  // Draw food
  ctx.fillStyle = "#f00";
  ctx.fillRect(food.x * cellSize, food.y * cellSize, cellSize, cellSize);
}

// Update game state on each tick
function update() {
  // Calculate new head position
  const newHead = {
    x: snake[0].x + direction.x,
    y: snake[0].y + direction.y
  };

  // Do nothing if direction is zero (game hasn’t started)
  if (direction.x === 0 && direction.y === 0) {
    draw();
    return;
  }

  // Wall or self collision ends the game
  if (
    newHead.x < 0 || newHead.x >= gridSize ||
    newHead.y < 0 || newHead.y >= gridSize ||
    snake.some(seg => seg.x === newHead.x && seg.y === newHead.y)
  ) {
    gameOver();
    return;
  }

  // Insert new head position
  snake.unshift(newHead);

  // Check if food eaten
  if (newHead.x === food.x && newHead.y === food.y) {
    score++;
    scoreDiv.textContent = `Score: ${score}`;
    food = spawnFood();
  } else {
    // Remove tail segment
    snake.pop();
  }

  // Redraw board
  draw();
}

// Handle game over, reset and restart
function gameOver() {
  clearInterval(intervalId);
  alert(`Game Over! Your score was ${score}.`);
  resetGame();
}

function resetGame() {
  snake = [{ x: Math.floor(gridSize / 2), y: Math.floor(gridSize / 2) }];
  direction = { x: 0, y: 0 };
  food = spawnFood();
  score = 0;
  scoreDiv.textContent = `Score: ${score}`;
  startGame();
}

// Start game loop according to selected level
function startGame() {
  clearInterval(intervalId);
  let speed;
  switch (levelSelect.value) {
    case "easy":
      speed = 200;
      break;
    case "hard":
      speed = 80;
      break;
    case "medium":
    default:
      speed = 125;
      break;
  }
  intervalId = setInterval(update, speed);
}

// Control snake with arrow keys, prevent reversing direction

document.addEventListener("keydown", e => {
  switch (e.key) {
    case "ArrowUp":
      if (direction.y !== 1) direction = { x: 0, y: -1 };
      break;
    case "ArrowDown":
      if (direction.y !== -1) direction = { x: 0, y: 1 };
      break;
    case "ArrowLeft":
      if (direction.x !== 1) direction = { x: -1, y: 0 };
      break;
    case "ArrowRight":
      if (direction.x !== -1) direction = { x: 1, y: 0 };
      break;
  }
});

// Restart game when level selection changes
levelSelect.addEventListener("change", () => {
  startGame();
});

// Initialize score display and start game
scoreDiv.textContent = `Score: ${score}`;
draw();
startGame();
