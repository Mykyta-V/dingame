# Dinosaur Game

A simple 2D dinosaur game built with pygame, inspired by the classic Chrome dinosaur dash game.

## Overview

This is a work-in-progress pygame application featuring a dinosaur character against a scrolling background. The game runs at 15 FPS and displays a persistent dinosaur sprite on the left side of the screen while the background continuously scrolls from right to left.

## Requirements

- Python 3.x
- pygame

## Setup & Installation

1. Install pygame:
```bash
pip install pygame
```

2. Ensure the following image assets are in the `images/` folder:
   - `dinosaur.png` - The dinosaur character sprite
   - `fon.png` - The background image
   - `bones.png` - The window icon

## How to Run

```bash
python game.py
```

## Features

- **Scrolling Background**: The background continuously moves left, creating a sense of forward motion
- **Static Dinosaur**: A dinosaur sprite displayed at a fixed position on the left side of the screen
- **Window Management**: Close the game window to exit

## Game Specifications

- **Resolution**: 900x300 pixels
- **FPS**: 15 frames per second
- **Title**: Dinosaur Game

## Future Improvements

- Add dinosaur jump mechanics
- Implement obstacles to avoid
- Add collision detection
- Score system
- Difficulty progression
- Sound effects

## Project Structure

```
Dingame/
├── game.py          # Main game file
├── Readme.md        # This file
└── images/          # Image assets
    ├── dinosaur.png
    ├── fon.png
    └── bones.png
```

## Controls

Currently, the game has no interactive controls beyond closing the window.
