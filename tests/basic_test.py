import pytest
from fuzzy_dictionary.FuzzyDict import FuzzyDict


def test_lookup_exact():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    assert d['Toronto Maple Leafs'] == 1967

def test_lookup_fuzzy_0():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    assert d['Toronto Maple Laughs'] == 1967


def test_lookup_fuzzy1():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    assert d['toronto maple leafs'] == 1967


def test_lookup_fuzzy_2():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    assert d['tronto mlp lfs'] == 1967


def test_no_key_empty():
    d = FuzzyDict()
    with pytest.raises(KeyError):
        _ = d['Tampa Bay Lightning']


def test_no_key_nonempty():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    with pytest.raises(KeyError):
        _ = d['Winnipeg Maple Leafs']

def test_get_default():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    assert not d.get('Winnipeg Jets')


def test_get_default_override():
    d = FuzzyDict()
    d['Toronto Maple Leafs'] = 1967
    assert d.get('Winnipeg Maple Leafs', -1) == -1


def test_weak_threshold_no_default():
    d = FuzzyDict(threshold=15)
    d['Toronto Maple Leafs'] = 1967
    assert d.get('Winnipeg Maple Leafs') == 1967


def test_weak_threshold_default():
    d = FuzzyDict(threshold=15)
    d['Toronto Maple Leafs'] = 1967
    assert d.get('Winnipeg Maple Branches', -1) == 1967


def test_multilookup_0():
    d = FuzzyDict(threshold=75)
    d['Toronto Maple Leafs'] = 1967
    d['Calgary Flames'] = 1989
    d['Vancouver Canucks'] = -1
    d['Montreal Canadians'] = 1992

    assert d['Montreal Canadians'] == 1992

def test_multilookup_1():
    d = FuzzyDict(threshold=75)
    d['Toronto Maple Leafs'] = 1967
    d['Calgary Flames'] = 1989
    d['Vancouver Canucks'] = -1
    d['Montreal Canadians'] = 1992

    assert d['Flames Calgary'] == 1989


def test_multilookup_2():
    d = FuzzyDict(threshold=75)
    d['Toronto Maple Leafs'] = 1967
    d['Calgary Flames'] = 1989
    d['Vancouver Canucks'] = -1
    d['Montreal Canadians'] = 1992

    assert d['Van canucks'] == -1


def test_len_empty():
    d = FuzzyDict(threshold=75)
    assert len(d) == 0


def test_len_nonempty():
    d = FuzzyDict(threshold=75)
    d['Toronto Maple Leafs'] = 1967
    d['Calgary Flames'] = 1989
    d['Vancouver Canucks'] = -1
    d['Montreal Canadians'] = 1992
    assert len(d) == 4
