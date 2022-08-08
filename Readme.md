# Fallout Dice Roll
A simple command line tool for rolling Combat Dice from the Fallout TTRPG

## Installation
Clone this repository to a desired location.
```powershell
git clone https://github.com/krdehli/fallout_dice_roll.git
```

Alternatively you can download the source code in compressed form from the Releases page.

## Usage
This repository contains two runnable scripts: `roll.py` and `convert.py`.
`roll.py` rolls a given number of combat dice, while `convert.py` converts a list of d6 rolls into
their respective combat rolls.

Roll four combat dice:
```powershell
./roll.py 4
```
Possible output:
```
Rolls: [1 1] [1 0] [0 0] [0 0]
Total damage: 2
Total effects: 1
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

You must run these scripts using a Python 3 interpreter. On most platforms, you can simply execute
the scripts themselves and python will automatically be invoced, provided it is installed.
If this fails you may have to invoce the Python 3 interpreter manually, like below.

```powershell
python ./convert.py 1 2 3 4 5 6
```
or
```powershell
python3 ./convert.py 1 2 3 4 5 6
```

## Requirements
You need a Python 3 interpreter to run the script.
