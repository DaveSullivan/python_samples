""" File of tests used to implement the lexicon class using a 
"Test First" method whereby the lexicon class was built up to eventually cause all tests here to succeed. This code was taken directly from: 
http://learnpythonthehardway.org/book/ex48.html
"""

from nose.tools import *
from scanner import lexicon

lex = lexicon.lexicon()
def test_directions():
    assert_equal(lex.scan("north"), [('direction', 'north')])
	
def test_directions2():	
    result = lex.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lex.scan("go"), [('verb', 'go')])
    result = lex.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])
						  
def test_stops():
    assert_equal(lex.scan("the"), [('stop', 'the')])
    result = lex.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])
						  
def test_nouns():
    assert_equal(lex.scan("bear"), [('noun', 'bear')])
    result = lex.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])
						  
def test_numbers():
    assert_equal(lex.scan("1234"), [('number', 1234)])
    result = lex.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])
						  
def test_errors():
    assert_equal(lex.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lex.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])