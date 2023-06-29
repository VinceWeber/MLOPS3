import sys
sys.path+=['../src']

# content of test_sample.py

from My_simple_function import *

#def test_bad_answer():
#    assert func(3) == 4

def test_good_answer():
    assert func(4) == 5