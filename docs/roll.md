# roll.py

## Syntax
```
roll.py [-h] [--history_file FILE] [-a | -n | -u] NUM_ROLLS
```

## Description
Rolls a given number of Fallout Combat Dice and yields a combined result.  
The output is in the format:
```
Rolls: <individual rolls>
Total damage: <total damage>
Total effects: <total effects>
```

The individual rolls are "cutely" represented with the following unicode symbols wrapped in square 
brackets:
  - `[•]` 1 damage, 0 effects <!-- &#8226; -->
  - `[⠡]` 2 damage, 0 effects <!-- &#10273; -->
  - `[☺]` 1 damage, 1 effect <!-- &#9786; -->
  - `[ ]` 0 damage, 0 effects

To display this properly, your terminal must support unicode output. Alternatively, if the `--ascii` 
flag is passed or the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` is set to "ascii", the 
rolls will instead be represented with the following ASCII symbols:
brackets:
  - `[.]` 1 damage, 0 effects
  - `[:]` 2 damage, 0 effects
  - `[O]` 1 damage, 1 effect 
  - `[ ]` 0 damage, 0 effects

All rolls are recorded in a history file. This file is stored as `roll_history` in the current 
working directory by default. The filename and filepath of the history file can be changed by 
passing the `--history_file` option to the roll command, or by setting the environment variable 
`FALLOUT_DICE_ROLL_HISTORY_FILE` to the desried filepath.

## Examples
### Example 1: Roll four combat dice
The simplest and most common usage of the `roll.py` command.
```powershell
.\roll.py 4
```
Possible output:
```
Rolls: [☺] [•] [ ] [ ]
Total damage: 2
Total effects: 1
```

### Example 2: Roll 3 combat dice with ASCII only output
Rolls 3 combat dice and displays the result in ASCII. Can be used if unicode is not supported by 
your terminal.
```powershell
.\roll.py -a 3
```
Possible output:
```
Rolls: [ ] [O] [O]
Total damage: 2
Total effects: 2
```
The same output can be acheived by setting the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` 
to "ascii" (without quttation marks, case-insenstive). If your terminal doesn't support unicode, 
it is recommended that you set this environment variable to "ascii" or "numeric" so that you don't 
have to specifiy a format option every time you invoke the command.

### Example 3: Roll 7 combat dice with a custom roll history location
Rolls 7 combat dice and records the result in the file `C:\fallout_dice_roll\history`.
```powershell
.\roll.py 7 --history_file C:\fallout_dice_roll\history
```
Possible output:
```
Rolls: [•] [⠡] [ ] [ ] [•] [☺] [•]
Total damage: 6
Total effects: 1
```
To set the history file path for every invocation of the command, you can set the environment 
variable `FALLOUT_DICE_ROLL_HISTORY_FILE` to the desired filepath, which would be 
`C:\fallout_dice_roll\history` in this case.

## Parameters

### NUM_ROLL
Specifies the number of combat dice to roll.  
Must be a strictly positive integer.

**Type**: Integer  
**Default**: None

---

### --history_file
Specifies the file in which the roll is recorded. If the file doesn't already exist, it is created.

To set the history file path for every invocation of the command, you can set the environment 
variable `FALLOUT_DICE_ROLL_HISTORY_FILE` to the desired filepath. Note however, that if the 
`--history_file` option is specified, it supersedes the path defined in the environment variable. 

**Type**: Filepath  
**Default**: ./roll_history

---

### --ascii, -a
Specifies that the output should use ASCII compatible characters.

You can set the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` to "ascii" to set this as the
default behaviour. 

**Type**: Flag  
**Default**: None

---

### --numeric, -n
Specifies that the output should use numbers instead of symbols. The rolls will be 
represented with self-explanatory pairs of numbers wrapped in square brackets.

You can set the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` to "numeric" to set this as the
default behaviour. 

**Type**: Flag  
**Default**: None

---

### --unicode, -u
Specifies that the output should use fancy unicode characters. This is the default behaviour.

You can set the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` to "unicode" to set this as the
default behaviour, although this is redundant.

**Type**: Flag  
**Default**: None

---

### --help, h
Show help message.

**Type**: Flag  
**Default**: None
