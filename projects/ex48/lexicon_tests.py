from nose.tools import *
import lexicon

def test_directions():
    assert_equal(lexicon.scan('north'), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicion.scan("go kill eat")
    assert_equal(reult, [('verb', 'go'),
                         ('verb', 'kill'),
                         ('verb', 'eat')])


