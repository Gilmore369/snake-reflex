"""Unit tests for the snake game logic.

These tests exercise the helper functions defined in
``snake_reflex/snake_game_logic.py``.  They verify that food is spawned
correctly, collisions are detected appropriately, and that the snake grows
when consuming food.
"""

import pytest

from snake_reflex.snake_game_logic import (
    spawn_food,
    is_collision,
    SnakeState,
    move_snake,
)



def test_spawn_food_not_on_snake():
    """Food should never spawn on a cell occupied by the snake."""
    snake = [(0, 0), (1, 0), (2, 0)]
    grid_size = 5
    # Generate multiple times to increase confidence
    for _ in range(20):
        food = spawn_food(snake, grid_size)
        assert food not in snake
        assert 0 <= food[0] < grid_size and 0 <= food[1] < grid_size


def test_wall_collision():
    """Positions outside the board should be detected as collisions."""
    snake = [(1, 1)]
    grid_size = 5
    assert is_collision((-1, 0), snake, grid_size)
    assert is_collision((grid_size, 0), snake, grid_size)
    assert is_collision((0, -1), snake, grid_size)
    assert is_collision((0, grid_size), snake, grid_size)


def test_self_collision():
    """Moving into the body of the snake should be reported as a collision."""
    snake = [(2, 2), (2, 3), (2, 4)]
    assert is_collision((2, 3), snake, grid_size=5)


def test_move_snake_growth_and_normal_move():
    """The snake should grow when eating food and maintain length otherwise."""
    # Initial state: snake of length 3 heading right toward food at (3,2)
    initial_state = SnakeState(body=[(2, 2), (2, 3), (2, 4)], food=(3, 2), score=0, grid_size=5)
    # First move: eats food and grows
    first_state = move_snake(initial_state, (1, 0))
    assert first_state is not None
    assert len(first_state.body) == len(initial_state.body) + 1
    assert first_state.score == 1
    assert first_state.body[0] == (3, 2)

    # Second move: no food at next position, should not grow
    second_state = move_snake(first_state, (1, 0))
    assert second_state is not None
    assert len(second_state.body) == len(first_state.body)
    assert second_state.score == 1
