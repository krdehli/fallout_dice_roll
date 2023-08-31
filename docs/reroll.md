# reroll.py

## Syntax
```
reroll.py [-h] [-r ROLL_INDEX] [--history_file FILE] [-a | -n | -u] DICE_INDECES [DICE_INDECES ...]
```

## Description
TODO

## Examples
TODO

## Parameters

### DICE_INDECES
TODO

| Type      | Position | Default |
| --------- | -------- | ------- |
| Int list  | 0        | None    |

### --roll_index
TODO

| Type      | Aliases | Position | Default           |
| --------- | ------- | -------- | ----------------- |
| Int       | -r      | Named    | -1                |

### --ascii
Specifies that the output should use ASCII compatible characters.

You can set the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` to "ascii" to set this as the
default behaviour. 

| Type      | Aliases | Position | Default           |
| --------- | ------- | -------- | ----------------- |
| Flag      | -a      | Named    | None              |

### --numeric
Specifies that the output should use numbers instead of symbols. The rolls will be 
represented with self-explanatory pairs of numbers wrapped in square brackets.

You can set the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` to "numeric" to set this as the
default behaviour. 

| Type      | Aliases | Position | Default           |
| --------- | ------- | -------- | ----------------- |
| Flag      | -n      | Named    | None              |

### --uniode
Specifies that the output should use fancy unicode characters. This is the default behaviour.

You can set the environment variable `FALLOUT_DICE_ROLL_OUT_FORMAT` to "unicode" to set this as the
default behaviour, although this is redundant.

| Type      | Aliases | Position | Default           |
| --------- | ------- | -------- | ----------------- |
| Flag      | -u      | Named    | None              |


### --help
Show help message.

| Type      | Aliases | Position | Default           |
| --------- | ------- | -------- | ----------------- |
| Flag      | -h      | Named    | None              |
