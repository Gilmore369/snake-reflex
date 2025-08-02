"""
Game logic utilities for the classic Snake game.

This module encapsulates a few functions that mirror the behaviour of the
JavaScript implementation used in the public facing game.  Having the core
logic in Python makes it straightforward to write unit tests using pytest.

Functions provided:
* ``spawn_food`` selects a random free cell on the board that is not
  currently occupied by the snake.
* ``is_collision`` determines whether a coordinate collides with either
  the walls of the board or the snake's own body.
* ``move_snake`` advances the snake in a given direction and handles
  growth when food is consumed.

The default ``grid_size`` matches the 20×20 board used in the game.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Tuple, Optional


Coordinate = Tuple[int, int]


@dataclass
class SnakeState:
    """Represents the state of the snake on the board.

    Attributes
    ----------
    body:
        A list of coordinates representing the snake segments.  The first
        coordinate is the head and subsequent values are the body.
    food:
        The coordinate where the current food resides.
    score:
        The current score for the snake (number of foods eaten).
    grid_size:
        The size of the playing field.  Defaults to 20 as used in the JS
        implementation.
    """

    body: List[Coordinate]
    food: Coordinate
    score: int = 0
    grid_size: int = 20


def spawn_food(snake: List[Coordinate], grid_size: int = 20) -> Coordinate:
    """Return a random coordinate not occupied by the snake.

    Parameters
    ----------
    snake:
        List of (x, y) tuples representing the snake's body.
    grid_size:
        The width and height of the board.

    Returns
    -------
    Coordinate
        A tuple representing the position of the new food.
    """
    free_positions = [
        (x, y)
        for x in range(grid_size)
        for y in range(grid_size)
        if (x, y) not in snake
    ]
    if not free_positions:
        raise ValueError("No free positions available to spawn food.")
    return random.choice(free_positions)


def is_collision(pos: Coordinate, snake: List[Coordinate], grid_size: int = 20) -> bool:
    """Return True if the given position collides with the wall or the snake's body.

    Parameters
    ----------
    pos:
        Proposed head coordinate of the snake.
    snake:
        Current snake body.
    grid_size:
        The width and height of the board.

    Returns
    -------
    bool
        True if collision would occur, False otherwise.
    """
    x, y = pos
    # Check walls
    if x < 0 or y < 0 or x >= grid_size or y >= grid_size:
        return True
    # Check self collision
    return pos in snake


def move_snake(state: SnakeState, direction: Coordinate) -> Optional[SnakeState]:
    """Advance the snake in the specified direction.

    If the snake consumes food at the next position, it will grow and new food
    will be spawned.  If the movement results in collision with a wall or
    itself, ``None`` is returned to indicate game over.

    Parameters
    ----------
    state:
        The current state of the snake (body, food, score, grid_size).
    direction:
        A tuple (dx, dy) indicating the movement direction.

    Returns
    -------
    Optional[SnakeState]
        The updated state if the move is valid, otherwise ``None``.
    """
    head_x, head_y = state.body[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    if is_collision(new_head, state.body, state.grid_size):
        return None

    new_body = [new_head] + state.body  # grow at head
    ate_food = new_head == state.food
    if ate_food:
        new_score = state.score + 1
        new_food = spawn_food(new_body, state.grid_size)
    else:
        new_body.pop()  # remove tail if not eating
        new_score = state.score
        new_food = state.food
    return SnakeState(body=new_body, food=new_food, score=new_score, grid_size=state.grid_size)
