# Conway's Game of Life

This implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) uses the Pygame library to offer an interactive simulation of the game. Conway's Game of Life is a cellular automaton created by British mathematician John Conway and is a zero-player game, so its evolution is determined by its initial state and requires no further input.

I have also created a randomised [CLI version of this here](https://github.com/zakmoCA/cli-conways-game-of-life) in C, which was too ambitious at first as I am currently just learning the C language, so the Python version came first. The C-version I may be expanding to include a GUI with the SDL library and to allow the user to set the initial state of the grid too.

## Installation and Running the Game

### Prerequisites

- Python 3.11 or higher

### Setup

**Clone the repository:**

```
git clone https://github.com/zakmoCA/py-conways-game-of-life.git
```

**Navigate to the repository root directory:**

```
cd py-conways-game-of-life
```

### Prepare the Setup Script

Before running the setup script, we need to make sure its got the necessary permissions to execute, so in the terminal we'll run:

```
chmod +x setup.sh
```

**And then we'll run the script:**

```
./setup.sh
```

## Game Controls

- **SPACE:** Start/Pause the game.
- **Mouse Click:** Add/Remove cells.
- **C:** Clear the grid.
- **R:** Randomly populate the grid.


