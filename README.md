# pyway

*Pyway is a simple Python class for simulating Conway's Game of Life*

Example:

```python
from pyway import Game

# Instantiate a Game object
C = Game()

# Get random initial conditions on a 100 x 100 grid
C.initial_conditions(100, 100)

# Generate and save an animation using default settings
C.make_animation()

```
![](docs/cogl1000g10s.gif)

## Install

Clone this repository and install a development version using `pip`:
```
pip install -e .
```
