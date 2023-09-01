# reroll.py

## Syntax
```
reroll.py [-h] [-r ROLL_INDEX] [--history_file FILE] [-a | -n | -u] DICE_INDECES [DICE_INDECES ...]
```

## Description
Rerolls one or more dice in a previous combat roll. The output is the same as [`roll.py`](roll.md),
except that the specific dice that were rerolled will be underlined.

<!--
## Examples
TODO
-->

## Parameters

### DICE_INDECES
Indeces of the desired dice to reroll. The indeces start at 1.

**Type**: Integer list  
**Default**: None

---

### --roll_index
Non-zero index of the roll to reroll. Positive indeces count forwards from the oldest roll, negative 
indeces count backwards from the most recent roll.

**Type**: Integer
**Default**: -1

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
