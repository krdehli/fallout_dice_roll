# Fallout Dice Roll
A simple set of command line tools for rolling Combat Dice from the Fallout TTRPG.

## Installation
Clone this repository to a desired location.
```powershell
git clone https://github.com/krdehli/fallout_dice_roll.git
```

Alternatively you can download the source code in compressed form from the Releases page.

## Usage
This repository contains the following runnable python scripts. Documentation for the specific
commands can be found in the `docs` folder or by clicking the links in the table below.

| Script                          | Description                                                    |
| ------------------------------- | -------------------------------------------------------------- | 
| [`roll.py`](docs/roll.md)       | Rolls a given number of combat dice                            |
| [`convert.py`](docs/convert.md) | Converts a list of d6 rolls into their respective combat rolls |
| [`history.py`](docs/history.md) | Displays your roll history                                     |
| [`reroll.py`](docs/reroll.md)   | Rerolls chosen dice in a previous roll                         |

You must run these scripts using a Python 3 interpreter. On most platforms, you can simply execute
the scripts themselves and python will automatically be invoked, provided it is installed.
If this fails you may have to invoke the Python 3 interpreter manually, like below.

```powershell
python ./roll.py 4
```
or
```powershell
python3 ./roll.py 4
```

Convert some d6 rolls:
```powershell
./convert.py 1 2 3 4 5 6
```
Output:
```
Rolls: [1 0] [2 0] [0 0] [0 0] [1 1] [1 1]
Total damage: 5
Total effects: 2
```



## Requirements
You need a Python version 3.11 (or later) interpreter to run the script.
