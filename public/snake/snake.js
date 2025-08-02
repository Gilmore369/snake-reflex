const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const grid = 20;
let count = 0;
let snake = [{ x: 10, y: 10 }];
let dx = 0, dy = 0;
let food = { x: 15, y: 15 };

function loop() {
  requestAnimationFrame(loop);
  if (++count < 4) return;
  count = 0;
  ctx.fillStyle = 'black';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Mover la serpiente
  snake.unshift({ x: snake[0].x + dx, y: snake[0].y + dy });
  if (snake[0].x === food.x && snake[0].y === food.y) {
    food = {
      x: Math.floor(Math.random() * (canvas.width / grid)),
      y: Math.floor(Math.random() * (canvas.height / grid)),
    };
  } else {
    snake.pop();
  }

  // Dibujar comida
  ctx.fillStyle = 'red';
  ctx.fillRect(food.x * grid, food.y * grid, grid - 2, grid - 2);

  // Dibujar serpiente
  ctx.fillStyle = 'lime';
  snake.forEach(seg =>
    ctx.fillRect(seg.x * grid, seg.y * grid, grid - 2, grid - 2)
  );
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowLeft' && dx === 0)  { dx = -1; dy = 0; }
  if (e.key === 'ArrowUp'   && dy === 0)  { dx = 0; dy = -1; }
  if (e.key === 'ArrowRight'&& dx === 0)  { dx = 1; dy = 0; }
  if (e.key === 'ArrowDown' && dy === 0)  { dx = 0; dy = 1; }
});

loop();
