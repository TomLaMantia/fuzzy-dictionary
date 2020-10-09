# fuzzy-dictionary
A dictionary-like class that supports fuzzy key lookups, written in Python.

## Installation
Run `pip install .` in the root directory of this repository.

## Examples:
```
from fuzzy_dictionary.FuzzyDict import FuzzyDict

>>> last_cup_win = FuzzyDict(threshold=75)
>>> last_cup_win['Montreal CanadiAns'] = 1992
>>> last_cup_win['Montreal CanadiEns']
1992
>>> last_cup_win['montreal canadians']
1992
```

The `FuzzyDict` class also supports standard methods, such as `len` and `get`
```$xslt
>>> last_cup_win['Montreal CanadiAns'] = 1992
>>> last_cup_win['Tampa Bay Lightning'] = 2020
>>> last_cup_win['Toronto Maple Leafs'] = 1992

>>> len(last_cup_win)
>>> 3

>>> last_cup_win.get('Buffalo Sabres', -1)
>>> -1
```

In this example, `threshold` determines how much fuzziness is tolerated.
For more information, see https://github.com/seatgeek/fuzzywuzzy.
```
>>> last_cup_win = FuzzyDict(threshold=99)
>>> last_cup_win['Toronto Maple Leafs']
1967

>>> last_cup_win['Toronto Maple Leaf']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".\site-packages\fuzzy_dictionary\FuzzyDict.py", line 19, in __getitem__
    raise KeyError
```
