# convert.py

## Syntax
```
convert.py [-h] [--history_file FILE] [-a | -n | -u] ROLL [ROLL ...]
```

## Description
Converts a list of d6 rolls to their respective combat dice rolls and yields a combined result.
Conversion is performed according to the following table:

| D6 | Combat Die |
| -- | ---------- |
|  1 | `[•]`      |
|  2 | `[⠡]`      |
|  3 | `[ ]`      |
|  4 | `[ ]`      |
|  5 | `[☺]`      |
|  6 | `[☺]`      |

The output format is exactly identical to [`roll.py`](roll.md).

## Examples

### Example 1: Convert d6 rolls
Converts one of each possible d6 roll to combat dice rolls.

```powershell
.\convert.py 1 2 3 4 5 6
```
Output:
```
Rolls: [•] [⠡] [ ] [ ] [☺] [☺]
Total damage: 5
Total effects: 2
```

## Parameters

### ROLL
Specifies the d6 rolls to convert.  
At least one roll must be given, and each one must be in the inclusive range [1, 6].

**Type**: Integer list
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
