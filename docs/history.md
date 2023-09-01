# history.py

## Syntax
```
history.py [-h] [--clear] [--history_file FILE] [-a | -n | -u]
```

## Description
Lists or clears your roll history.  
Every roll will be displayed in the same format as [`roll.py`](roll.md), prefixed with its 
index (starting at 1). The roll history does not differentiate between rolls resulting from the 
`roll` command, `convert` command, or `reroll` command.

Specifying the `--clear` option removes all entries from the history file.

## Examples

### Example 1: List roll history
Lists the roll history.

```powershell
.\history.py
```
Possible output:
```
* Roll #1 *
Rolls: [☺] [ ] [ ] [☺]
Total damage: 2
Total effects: 2
***

* Roll #2 *
Rolls: [•] [•] [ ] [•] [⠡] [ ] [☺]
Total damage: 6
Total effects: 1
***

* Roll #3 *
Rolls: [☺] [☺] [☺]
Total damage: 3
Total effects: 3
***
```

### Example 2: Clear history
Erases the entire roll_history.

```powershell
.\history.py --clear
```
Output:
```
Are you sure you want to clear the entire roll history? ([y]es/[n]o):
```
The user will always be prompted for a confirmation when clearing the history.

### Example 3: List history with a custom roll history location
Lists the roll history recorded in the file `C:\fallout_dice_roll\history`.

```powershell
.\history.py --history_file C:\fallout_dice_roll\history
```
Possible output:
```
* Roll #1 *
Rolls: [⠡] [☺] [☺] [☺] [ ]
Total damage: 5
Total effects: 3
***

* Roll #2 *
Rolls: [☺] [☺] [☺] [ ] [☺]
Total damage: 4
Total effects: 4
***

* Roll #3 *
Rolls: [☺] [ ] [ ] [ ] [ ] [ ] [⠡] [☺]
Total damage: 4
Total effects: 2
***
```

### Example 4: Clear history with a custom roll history location
Erases the entire roll_history recorded in the file `C:\fallout_dice_roll\history`.

```powershell
.\history.py --clear --history_file C:\fallout_dice_roll\history
```
Output:
```
Are you sure you want to clear the entire roll history? ([y]es/[n]o):
```

## Parameters

### --clear
Clears the entire history instead of listing it. The history file will still exist, but will be 
empty.

A yes/no prompt will ask for confirmation when running the command with this option.

**Type**: Flag  
**Default**: None

### --history_file
Specifies the file in which the roll history is recorded. 

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
