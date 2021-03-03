import pytest
from fuzzy_dictionary.FuzzyDict import FuzzyDict

d = FuzzyDict()
d['Toronto Maple Leafs'] = 1967

assert d['Toronto Maple Leafs'] == 1967
assert d['Toronto Maple Laughs'] == 1967
assert d['toronto maple leafs'] == 1967
assert d['tronto mlp lfs'] == 1967

with pytest.raises(Exception):
    _ = d['Tampa Bay Lightning']

with pytest.raises(Exception):
    _ = d['Winnipeg Maple Leafs']

assert not d.get('Winnipeg Jets')
assert d.get('Winnipeg Maple Leafs', -1) == -1

d = FuzzyDict(threshold=15)
d['Toronto Maple Leafs'] = 1967
assert d.get('Winnipeg Maple Leafs') == 1967
assert d.get('Winnipeg Maple Leafs', -1) == 1967

d = FuzzyDict(threshold=75)
d['Toronto Maple Leafs'] = 1967
d['Calgary Flames'] = 1989
d['Vancouver Canucks'] = -1
d['Montreal Canadians'] = 1992

assert d['Montreal Canadians'] == 1992
assert d['Flames Calgary'] == 1989
assert d['Van canucks'] == -1
assert len(d) == 4

with pytest.raises(KeyError):
    _ = d['Buffalo Sabres']


